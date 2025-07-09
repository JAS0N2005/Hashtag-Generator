import re
from config import EXCLUDED_TYPE_HASHTAGS

def apply_type_hashtags(type_field: str) -> list:
    """
    Fallback: Use the entire Type field as a PascalCase hashtag,
    but first normalize so hyphens → spaces, strip all other
    punctuation (while keeping accented letters), and then
    build the tag.  Exclude via EXCLUDED_TYPE_HASHTAGS.
    """
    tf_raw = str(type_field) or ""
    # 1) Turn hyphens into spaces
    tf_norm = tf_raw.replace('-', ' ')
    # 2) Strip everything except letters (incl. accents), digits, underscore & whitespace
    tf_norm = re.sub(r'[^\w\s]', '', tf_norm, flags=re.UNICODE)
    # 3) Split into words
    parts = [w for w in tf_norm.split() if w]
    if not parts:
        return []

    # 4) Build PascalCase hashtag (accents remain)
    fallback = "#" + "".join(w.capitalize() for w in parts)
    fallback_lower = fallback.lower()

    # 5) Exclusion check (exact or singular→plural)
    excluded = {h.lower() for h in EXCLUDED_TYPE_HASHTAGS}
    if (fallback_lower in excluded or
        (fallback_lower.endswith("s") and fallback_lower[:-1] in excluded) or 
        (fallback_lower.endswith("es") and fallback_lower[:-2] in excluded)):
        return []

    return [fallback]
