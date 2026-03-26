import pandas as pd
from trie import Trie

# Reuse the same CSV-loading + filtering logic from search.py
# (imported here to avoid duplication — or copy-paste if you prefer standalone)
from search import search_data, merge_data, count_matches


# -------- Build Trie --------
def build_trie(search_words):
    df = merge_data(search_words)
    trie = Trie()

    for _, row in df.iterrows():
        entry = row.to_dict()
        entry["match_count"] = count_matches(row, search_words)
        key = row["Name"]
        trie.insert(key, entry)

    return trie


# -------- Final function for Trie --------
def get_sorted_results_for_trie(search_words):
    """
    Returns all matching perfumes sorted alphabetically by name.
    Drop-in counterpart to get_sorted_results_for_hashmap() in search.py.
    """
    trie = build_trie(search_words)
    return trie.get_sorted_entries()


# -------- Check --------
if __name__ == "__main__":
    results = get_sorted_results_for_trie(["vanilla", "blood orange"])

    for perfume in results:
        print(f"{perfume['Name']} | matches: {perfume['match_count']}")
