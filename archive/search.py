import pandas as pd

# -------- Search in clean database -----------

def search_data(search_words):
    df = pd.read_csv("fra_cleaned.csv", encoding="latin-1", sep=";")
    df.columns = df.columns.str.strip()

    cols = ["Top", "Middle", "Base"]

    search_words = [w.lower() for w in search_words]

    mask = df[cols].apply(
        lambda col: col.str.lower().apply(
            lambda cell: any(word in cell for word in search_words) if isinstance(cell, str) else False
        )
    ).any(axis=1)
    return df[mask]


# ----------- Check ----------------
# matches = search_data(["blood orange", "vanilla"])
# print(matches)

# ---------- Use second database for description ----------
def merge_data(search_words):
    filtered_df = search_data(search_words)

    df2 = pd.read_csv("fra_perfumes.csv", encoding="latin-1", sep=",")
    df2.columns = df2.columns.str.strip()

    # Check urls
    filtered_df["url"] = filtered_df["url"].str.lower().str.strip()
    df2["url"] = df2["url"].str.lower().str.strip()

    key = "url"
    print(len(set(filtered_df["url"]) & set(df2["url"])))
    cols_to_add = ["Top", "Middle", "Base"]

    result = pd.merge(
        df2,
        filtered_df[[key] + cols_to_add],
        on=key,
        how="inner"
    )

    return result

# ---------- Check final data base -----------------
print(merge_data(["aldehydes", "vanilla"]))