import pandas as pd

def apply_find_replace(df: pd.DataFrame, column: str, replacements: dict) -> pd.DataFrame:
    if column not in df.columns:
        return df

    def _replace(val):
        # Leave NaN (empty) values untouched
        if pd.isna(val):
            return val
        # Otherwise, do your literal replacements
        text = str(val)
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text

    df[column] = df[column].apply(_replace)
    return df
