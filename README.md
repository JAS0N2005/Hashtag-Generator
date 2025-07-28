# Hashtag Generator for Location Data

This repository provides a robust Python utility designed to automate the generation, normalization, and deduplication of hashtags for location-based data, especially for content related to places, food, entertainment, and more. The tool processes Excel workbooks containing multiple sheets and applies configurable rules for hashtag assignment, conflict resolution, and exclusion, producing a clean, consolidated final dataset.

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Configuration File (`config.py`)](#configuration-file-configpy)
  - [Map Explanations & When to Use](#map-explanations--when-to-use)
- [Rule Customization](#rule-customization)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Automatic Hashtag Generation:** Assigns hashtags to each row based on columns like "Type", "Name", and "About" using content and type rules.
- **Food-Specific Processing:** Sheets identified as food-related are handled with custom logic for food hashtags.
- **Conflict & Exclusion Handling:** Removes redundant, conflicting, or explicitly excluded hashtags.
- **Find-and-Replace Utility:** Cleans up "Opening_hours" and other columns as per custom rules.
- **Final Excel Export:** Consolidates all data into a single, clean Excel workbook ready for delivery or further analysis.

---

## How It Works

1. **Load Input Workbook:** Reads the source Excel file specified in `config.py`.
2. **Sheet Classification:** Distinguishes between food-related and other sheets using keywords.
3. **Hashtag Assignment:**
   - Non-food sheets: Assign hashtags based on content and type rules.
   - Food sheets: Assign hashtags using food-specific logic.
4. **Deduplication & Conflict Resolution:** Cleans up hashtags using configurable maps.
5. **Find-and-Replace:** Applies string replacements (e.g., for opening hours formatting).
6. **Export:** Saves the consolidated data to the location specified in `config.py`.

---

## Setup Instructions

### 1. Prerequisites

- Python 3.8+
- pip (Python package manager)

### 2. Create a virtual environment & install Dependencies using the command sequence given below

```sh
python -m venv venv

.\venv\scripts\activate

pip install -r requirements.txt
```

### 3. Configuration

Edit `config.py` to set:

- `INPUT_FILE`: Path to your source Excel file.
- `OUTPUT_FILE`: Path for the final output file.
- Optionally, customize rules and maps as needed (see below).

---

## Usage

Run the script from the command line:

```sh
python main.py
```

- The script will print progress logs and generate the output Excel file at the specified path.

---

## Configuration File (`config.py`)

This file holds all the **rules and mappings** that govern how hashtags are generated, excluded, or resolved.

### Key Maps and Settings

#### 1. `CONFLICT_HASHTAG_MAP`

**Purpose:**  
When a "dominant" hashtag is present in a row, this map specifies which *other* hashtags should be removed to avoid redundancy or conflict.

**Example Use:**
- If `#SuperMarkets` is present, then `#MarketStalls`, `#StreetMarkets`, and `#Vendors` will be removed.

```python
CONFLICT_HASHTAG_MAP = {
    "#SuperMarkets": {"#MarketStalls","#StreetMarkets","#Vendors"},
    "#Churches": {"#Church"},
    # ...more rules...
}
```

**When to use:**  
Use when you want to ensure higher-level or more general hashtags take precedence, and less relevant or redundant hashtags are suppressed.

---

#### 2. `EXCLUDED_TYPE_HASHTAGS`

**Purpose:**  
Defines hashtags that should *never* appear in the output, regardless of other rules.

**Example Use:**
- If `#FastFoodRestaurant` or `#Bar` appears, it will always be removed from the final hashtag list.

```python
EXCLUDED_TYPE_HASHTAGS = {
    "#FastFoodRestaurant",
    "#Bar",
    "#Cafe",
    # ...more...
}
```

**When to use:**  
Use for tags that are too generic, irrelevant, or should be blacklisted for business/content reasons.

---

#### 3. `CONTENT_RULES`

**Purpose:**  
Maps keywords (single words or phrases) to one or more hashtags. When a keyword is found in the "Type", "Name", or "About" fields, the corresponding hashtags are added.

**Example Use:**
- If "museum" is found, add `#Museums` and `#History`.
- If "church" is found, add `#Churches`, `#Praying`, and `#Religion`.

```python
CONTENT_RULES = {
    "museum": ["#Museums", "#History"],
    "church": ["#Churches", "#Praying", "#Religion"],
    # ...more...
}
```

**When to use:**  
Use for mapping specific terms or phrases to one or several relevant hashtags.

---

#### 4. `FOOD_SHEET_KEYWORDS`

**Purpose:**  
List of keywords used to identify food-related sheets.

**Example Use:**
If a sheet is named "Restaurants in Hanoi", it's classified as a food sheet.

```python
FOOD_SHEET_KEYWORDS = [
    "restaurants", "bars", "cafes", "nightlife",
    "bakery", "nightclubs", # ...more...
]
```

---

#### 5. `OMIT_WORDS`

**Purpose:**  
Words to ignore when generating fallback hashtags (to avoid overly generic tags).

**Example Use:**
- Words like "restaurant", "place", or "shop" are omitted from fallback hashtags.

---

#### 6. `ANIMAL_KEYWORDS` and `MARINE_KEYWORDS`

**Purpose:**  
Lists of animal and marine-related keywords. If any are present in a row, special hashtags like `#Wildlife` or `#MarineLife` are added.

---

### Example Row Processing

Suppose a row has:

- Type: `Supermarket`
- Name: `BigMart`
- About: `A popular place for groceries and snacks`

**Processing:**

- Content rules match "supermarket" → `#Markets`, `#RetailStores`, `#Supermarkets`
- Fallback type hashtag: `#Supermarket`
- Deduplication: If both singular and plural versions exist, only the plural is kept.
- Conflict removal: If `#SuperMarkets` is present, tags like `#MarketStalls` and `#Vendors` are removed.
- Exclusion: Any tag in `EXCLUDED_TYPE_HASHTAGS` is dropped.

---

## Rule Customization

You can extend or modify rules in `config.py` to adapt hashtag logic for your specific project or data.

- **Add new phrases or keywords** to `CONTENT_RULES` for your domain.
- **Update `CONFLICT_HASHTAG_MAP`** for new dominant/redundant hashtag pairs.
- **Expand `EXCLUDED_TYPE_HASHTAGS`** to keep unwanted tags out of your results.

---

## Examples

### Example 1: Conflict Map in Action

```python
CONFLICT_HASHTAG_MAP = {
    "#SuperMarkets": {"#MarketStalls", "#StreetMarkets", "#Vendors"}
}
```
- **If a row gets both `#SuperMarkets` and `#MarketStalls`, only `#SuperMarkets` remains.**

### Example 2: Exclusion Map

```python
EXCLUDED_TYPE_HASHTAGS = {
    "#FastFoodRestaurant", "#Bar", "#Cafe"
}
```
- **If any of these tags are produced, they are always removed.**

### Example 3: Content Rules

```python
CONTENT_RULES = {
    "museum": ["#Museums", "#History"],
    "art cafe": ["#ArtCafe"]
}
```
- **If "museum" appears in the Type or About column, the row gets `#Museums` and `#History`.**

---

## Contributing

Yours truly
Subhojyoti :]

---