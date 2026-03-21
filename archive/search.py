import pandas as pd


def search_data(search_words):
    df = pd.read_csv("fra_cleaned.csv", encoding="latin-1", sep=";")
    df.columns = df.columns.str.strip()

    cols = ["Top", "Middle", "Base"]

    words = [w.lower() for w in search_words]

    mask = df[cols].apply(
        lambda col: col.str.lower().apply(
            lambda cell: any(word in cell for word in search_words) if isinstance(cell, str) else False
        )
    ).any(axis=1)
    return df[mask]


#check
matches = search_data(["blood orange", "vanilla"])
print(matches)