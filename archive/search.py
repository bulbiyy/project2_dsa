import pandas as pd
from hashmap import HashMap

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

    result = result[["Name", "Gender", "Description", "Top", "Middle", "Base", "url"]]
    return result
# ---------- Check final data base -----------------
#print(merge_data(["aldehydessss"]))


# ---------- Count for hashmap ----------
def count_matches(row, search_words):
    count = 0
    for col in ["Top", "Middle", "Base"]:
        if isinstance(row[col], str):
            for word in search_words:
                if word in row[col].lower():
                    count += 1
    return count

# -------- Build hashmap -----------
def build_hashmap(search_words):
    df = merge_data(search_words)
    hm = HashMap()

    for _, row in df.iterrows():
        entry = row.to_dict()
        entry["match_count"] = count_matches(row, search_words)
        key = row["Name"]
        hm.insert(key, entry)

    return hm

# -------- Final function for hashmap -----------
def get_sorted_results_for_hashmap(search_words):
    hm = build_hashmap(search_words)
    return hm.get_sorted_entries()

# ------- Check hashmap ---------
# if __name__ == "__main__":
#     results = get_sorted_results_for_hashmap(["vanilla", "blood orange"])
#
#     for perfume in results:
#         print(f"{perfume['Name']} | matches: {perfume['match_count']}")