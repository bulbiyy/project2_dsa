from flask import Flask, request, jsonify
import time
import pandas as pd

from search import get_sorted_results_for_hashmap
from search_trie import get_sorted_results_for_trie

app = Flask(__name__)

from flask import send_file

@app.route("/")
def home():
    return send_file("AromaAtlas.html")

def load_notes():
    df = pd.read_csv("fra_cleaned.csv", encoding="latin-1", sep=";")
    notes = set()

    for col in ["Top", "Middle", "Base"]:
        for cell in df[col].dropna():
            parts = str(cell).lower().split(",")
            for p in parts:
                notes.add(p.strip())

    return sorted(notes)

ALL_NOTES = load_notes()

@app.route("/autocomplete")
def autocomplete():
    q = request.args.get("q", "").lower()

    matches = [n for n in ALL_NOTES if n.startswith(q)]
    return jsonify(matches[:10])

def build_tiers(results, notes, priority):
    tier1 = []
    tier2 = []
    tier3 = []

    for item in results:
        matched = []

        for layer in ["Top", "Middle", "Base"]:
            if isinstance(item[layer], str):
                for n in notes:
                    if n in item[layer].lower():
                        matched.append({
                            "note": n,
                            "layer": layer.lower()
                        })

        item_out = {
            "name": item["Name"],
            "brand": item.get("Gender", ""),
            "matched_notes": matched
        }

        match_count = item.get("match_count", 0)

        if match_count == len(notes):
            tier1.append(item_out)
        elif priority and any(m["note"] == priority for m in matched):
            tier3.append(item_out)
        else:
            tier2.append(item_out)

    return {
        "tier1": tier1,
        "tier2": tier2,
        "tier3": tier3
    }


@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()

    notes = data.get("notes", [])
    priority = data.get("priority", "")

    if not notes:
        return jsonify({"error": "No notes provided"})

    # -------- Hash Map --------
    t0 = time.perf_counter()
    hm_results = get_sorted_results_for_hashmap(notes)
    hm_time = (time.perf_counter() - t0) * 1000

    # -------- Trie --------
    t0 = time.perf_counter()
    trie_results = get_sorted_results_for_trie(notes)
    trie_time = (time.perf_counter() - t0) * 1000

    # -------- Format --------
    response = {
        "hashmap": {
            "time_ms": hm_time,
            "results": build_tiers(hm_results, notes, priority)
        },
        "trie": {
            "time_ms": trie_time,
            "results": build_tiers(trie_results, notes, priority)
        },
        "fastest": "hashmap" if hm_time < trie_time else "trie",
        "priority": priority
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)