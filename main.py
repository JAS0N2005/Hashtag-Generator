import pandas as pd
import os
from config import (
    INPUT_FOLDER, OUTPUT_FOLDER, FOOD_SHEET_KEYWORDS, EXCLUDED_TYPE_HASHTAGS,
    HASHTAGS_TARGET_INDEX, CONFLICT_HASHTAG_MAP, CSV_LOG
)
from utils import (
    normalize_columns, extract_existing,
    deduplicate_hashtags, move_column,
    consolidate_processed_sheets, init_logger,
    count_rows_xlsx, sanitize_filename
)
from replacement_rules import apply_find_replace
from content_rules import apply_content_hashtags
from type_rules import apply_type_hashtags
from food_rules import apply_food_only_hashtags

def process_city_file(input_file: str, output_file: str):
    # 1) Load workbook and drop the master sheet
    print("🕑  About to load workbook:", input_file, flush=True)
    xls = pd.ExcelFile(input_file)
    print("✅  Workbook loaded; sheets:", xls.sheet_names, flush=True)
    sheet_names = [
        name for name in xls.sheet_names
        if name not in ("MasterSheet", "Final MasterSheet", "Sheet1", "master_sheet")
    ]

    # 2) Parse only the remaining sheets into a dict
    sheets = {name: xls.parse(name) for name in sheet_names}

    # 3) Classify sheets into food vs non-food
    food_names = [
        name for name in sheet_names
        if any(kw.lower() in name.lower() for kw in FOOD_SHEET_KEYWORDS)
    ]
    non_food_names = [name for name in sheet_names if name not in food_names]
    print("▶️ Non-food tabs:", non_food_names)
    print("▶️  Food tabs  :", food_names)

    processed = {}
    total_rows = 0

    # 4) Process non-food sheets with content + type rules
    for name in non_food_names:
        df = normalize_columns(sheets[name])
        row_count = len(df)
        total_rows += row_count
        print(f"Processing '{name}' ({row_count} rows)")

        def update(row):
            existing_list, existing_set = extract_existing(row.get("HashTags", ""))
            # a) Content-based hashtags
            for tag in apply_content_hashtags(
                row.get("Name", ""),
                row.get("About", ""),
                row.get("Type", ""),
                existing_set
            ):
                if tag not in existing_set:
                    existing_list.append(tag)
                    existing_set.add(tag)
            # b) Type-based fallback hashtags
            for tag in apply_type_hashtags(row.get("Type", "")):
                if tag not in existing_set:
                    existing_list.append(tag)
                    existing_set.add(tag)
            return "\n".join(existing_list)  # Corrected line for new line join

        df["HashTags"] = df.apply(update, axis=1)
        processed[name] = df

    # 5) Process food sheets separately (combined into one FOOD sheet)
    if food_names:
        food_frames = []
        for name in food_names:
            df_food = normalize_columns(sheets[name])
            count = len(df_food)
            total_rows += count
            print(f"Loading food sheet '{name}' ({count} rows)")
            food_frames.append(df_food)
        combined = pd.concat(food_frames, ignore_index=True)
        print(f"Combined food rows: {len(combined)}")

        # Apply only the food-specific rules
        combined = apply_food_only_hashtags(combined)
        processed["FOOD"] = combined

    print(f"✅ Total rows to write: {total_rows}")

    # 6) Consolidate all processed frames and move the HashTags column
    final_dict = consolidate_processed_sheets(processed)
    for name, df in final_dict.items():
        final_dict[name] = move_column(df, "HashTags", HASHTAGS_TARGET_INDEX)

    # 7) One final de-dup + conflict + exclusion pass
    for name, df in final_dict.items():
        def clean(cell):
            tags = cell.splitlines() if isinstance(cell, str) else []
            cleaned = deduplicate_hashtags(
                tags,
                EXCLUDED_TYPE_HASHTAGS,
                CONFLICT_HASHTAG_MAP
            )
            return "\n".join(cleaned)  # Corrected line for new line join
        final_dict[name]["HashTags"] = final_dict[name]["HashTags"].apply(clean)

    # 8) Apply find-and-replace on the Opening_hours column
    REPLACEMENTS = {
        '. Hide open hours for the week': '',
        'to': '-',
        ',': ':',
        ';': '\n',  # Correct replacement for semicolons
    }
    for name, df in final_dict.items():
        final_dict[name] = apply_find_replace(df, 'Opening_hours', REPLACEMENTS)

    # 9) Save the final workbook after replacements
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        for name, df in final_dict.items():
            df.to_excel(writer, sheet_name=name, index=False)

    print(f"🎉 Saved final workbook to {output_file}")
    return total_rows

def main():
    # set up CSV logger
    log_file, log_writer = init_logger(CSV_LOG)
    # df = pd.read_csv(CSV_LOG, usecols=['City'])
    masters = ["MasterSheet", "Final MasterSheet", "Mastersheet", "master_sheet","mastersheet"]
    # Process each file in the input folder
    for filename in os.listdir(INPUT_FOLDER):
        if filename.endswith(".xlsx"):
            # Extract city name dynamically between "Cleaned" and "Data", excluding "Data"
            city_name_lower = filename.lower().split("cleaned")[1].split("data")[0].strip()  # Only get the city name
            city_name = sanitize_filename(city_name_lower).title()
            # faster membership check
            # if city_name in df['City'].values:
            #     print(f"{city_name} Done. Skipping to the next city")
            #     continue

            input_file = os.path.join(INPUT_FOLDER, filename)
            output_file = os.path.join(OUTPUT_FOLDER, f"FINAL {city_name}.xlsx")  # Output as FINAL <CityName>.xlsx
                        # 1) Try counting the master sheet
            total_rows = process_city_file(input_file, output_file) 
            master_rows = count_rows_xlsx(input_file, masters)

            if master_rows == 0:
                # Immediately log “Missing MasterSheet” and skip further tally logic
                log_writer.writerow([city_name, 0, 0, "Missing MasterSheet"])
                log_file.flush()
                print(f"LOGGER: {city_name} → ERROR: Missing MasterSheet")
                continue
        
            if master_rows!=total_rows: 
                log_writer.writerow([city_name, 0, 0, "ERROR: Not Tallied"])
                log_file.flush()
                print(f"LOGGER:{city_name}-VOLUME:{master_rows}-TOTAL:{total_rows}------>ERROR: Not Tallied")
                continue
        
            tally_status = "Tallied"
            log_writer.writerow([city_name,master_rows,total_rows,tally_status])
            log_file.flush()
            print(f"LOGGER:{city_name}-VOLUME:{master_rows}-TOTAL:{total_rows}------>{tally_status}")


    log_file.close()

if __name__ == "__main__":
    main()
