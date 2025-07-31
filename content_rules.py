import re
from config import (
    CONTENT_RULES, ANIMAL_KEYWORDS, WILDLIFE_TAG, MARINE_KEYWORDS, MARINE_LIFE_TAG
)

def apply_content_hashtags(name: str, about: str, type_field: str, existing_set: set) -> list:
    """
    1) Match keywords in CONTENT_RULES against tokens and phrases in name/about/type_field
    2) Add marine and wildlife tags based on token presence
    """
    name = name if isinstance(name, str) else ""
    about = about if isinstance(about, str) else ""
    type_field = type_field if isinstance(type_field, str) else ""

    # 1) Normalize and clean punctuation
    raw = f"{name} {about} {type_field}".lower()
    raw = raw.replace('-', ' ')                            # hyphens → spaces
    # keep letters (including accents), digits and whitespace; strip everything else
    raw = re.sub(r'[^\w\s]', '', raw, flags=re.UNICODE)
    
    # 2) Tokenize
    tokens = re.findall(r"\w+", raw)
    joined_text = " ".join(tokens)

    tags = []

    for keyword, candidates in CONTENT_RULES.items():
        # normalize keyword into space-separated words
        kw_norm = keyword.lower().replace('-', ' ')
        parts   = kw_norm.split()

        matched = False
        if len(parts) == 1:
            base    = re.escape(parts[0])
            pattern = rf"\b{base}(?:es|s)?\b"
            if re.search(pattern, joined_text):
                matched = True
        else:
            phrase = ' '.join(parts)
            # whole-phrase match with word boundaries
            pattern = rf"\b{re.escape(phrase)}\b"
            if re.search(pattern, joined_text):
                matched = True

        if matched:
            for tag in candidates:
                if tag not in existing_set:
                    tags.append(tag)

    # Wildlife detection
    if any(tok in ANIMAL_KEYWORDS for tok in tokens):
        if WILDLIFE_TAG not in existing_set and WILDLIFE_TAG not in tags:
            tags.append(WILDLIFE_TAG)

    # Marine-life detection
    if any(tok in MARINE_KEYWORDS for tok in tokens):
        if MARINE_LIFE_TAG not in existing_set and MARINE_LIFE_TAG not in tags:
            tags.append(MARINE_LIFE_TAG)

    return tags
