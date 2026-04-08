import time
from search import get_sorted_results_for_hashmap
from search_trie import get_sorted_results_for_trie


def compare(search_words):
    print(f"\n{'='*55}")
    print(f"Search words: {search_words}")
    print(f"{'='*55}")

    t0 = time.perf_counter()
    hm_results = get_sorted_results_for_hashmap(search_words)
    hm_time = time.perf_counter() - t0

    print(f"\n[HashMap]  {len(hm_results)} results  |  {hm_time*1000:.2f} ms")
    print(f"  Sort order: by match_count (descending)")
    for p in hm_results[:5]:
        print(f"    {p['Name']:40s} matches: {p['match_count']}")

    #Trie
    t0 = time.perf_counter()
    trie_results = get_sorted_results_for_trie(search_words)
    trie_time = time.perf_counter() - t0

    print(f"\n[Trie]     {len(trie_results)} results  |  {trie_time*1000:.2f} ms")
    print(f"  Sort order: alphabetical (A→Z)")
    for p in trie_results[:5]:
        print(f"    {p['Name']:40s} matches: {p['match_count']}")


    print(f"\n{'─'*55}")
    print(f"HashMap time : {hm_time*1000:.2f} ms")
    print(f"Trie time    : {trie_time*1000:.2f} ms")
    faster = "HashMap" if hm_time < trie_time else "Trie"
    ratio = max(hm_time, trie_time) / min(hm_time, trie_time)
    print(f"{faster} was {ratio:.1f}x faster for this query.")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    compare(["vanilla", "blood orange"])
    compare(["rose", "musk", "amber"])
