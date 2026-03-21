import pandas as pd


def search_data(search_word):
    df = pd.read_csv("fra_cleaned.csv", encoding="latin-1", sep=";")
    df.columns = df.columns.str.strip()

    cols = ["Top", "Middle", "Base"]

    mask = df[cols].apply(
        lambda col: col.str.lower().str.contains(search_word.lower(), na=False)
    ).any(axis=1)

    return df[mask]


#check
matches = search_data("blood orange")
print(matches)