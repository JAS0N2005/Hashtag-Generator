import re
from utils import extract_existing
from config import OMIT_WORDS, CONTENT_RULES

def apply_food_only_hashtags(df):
    """
    1) Normalize and clean punctuation in the Type field
    2) Tokenize and filter out OMIT_WORDS
    3) Apply CONTENT_RULES with unified matching (whole-word for single words, substring for phrases)
    4) Fallback: PascalCase hashtag from remaining tokens
    """
    original_cols = df.columns.tolist()
    omit_lower = {w.lower() for w in OMIT_WORDS}

    def update(row):
        existing_list, existing_set = extract_existing(row.get("HashTags", ""))

        # 1) Normalize and clean punctuation
        raw = str(row.get("Type", "")).lower()
        raw = raw.replace('-', ' ')
        raw = re.sub(r'[^\w\s]', '', raw, flags=re.UNICODE)


        # 2) Tokenize and filter
        tokens = re.findall(r"\w+", raw)
        filtered = []
        for tok in tokens:
            tl = tok.lower()
            if tl in omit_lower or (tl.endswith('s') and tl[:-1] in omit_lower):
                continue
            filtered.append(tok)

        cleaned_text = " ".join(filtered).lower()

        # 3) Unified CONTENT_RULES matching
        for phrase, tags in CONTENT_RULES.items():
            # Normalize keyword
            kw_norm = phrase.lower().replace('-', ' ')
            parts = kw_norm.split()
            matched = False
            if len(parts) == 1:
                # Whole-word match, allow s/es plurals
                base = re.escape(parts[0])
                pattern = rf"\b{base}(?:es|s)?\b"
                if re.search(pattern, cleaned_text):
                    matched = True
            else:
                # Multi-word phrase match
                if kw_norm in cleaned_text:
                    matched = True

            if matched:
                for tag in tags:
                    if tag not in existing_set:
                        existing_list.append(tag)
                        existing_set.add(tag)

        # 4) Fallback PascalCase
        if filtered:
            fallback = "#" + "".join(tok.capitalize() for tok in filtered)
            if fallback not in existing_set:
                existing_list.append(fallback)
                existing_set.add(fallback)

        return "\n".join(existing_list)

    df["HashTags"] = df.apply(update, axis=1)
    # Restore original column order
    if "HashTags" in original_cols:
        return df[original_cols]
    else:
        cols = [c for c in original_cols if c != "HashTags"] + ["HashTags"]
        return df[cols]
