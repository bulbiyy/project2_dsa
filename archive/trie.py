class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.entries: list[dict] = []   # perfume dicts stored at word-end node
        self.is_end: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self._size = 0

    #Core insert
    #Insert a perfume entry under the given key
    def insert(self, key: str, entry: dict):

        node = self.root
        for char in key.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        if not node.is_end:
            node.is_end = True
            self._size += 1

        node.entries.append(entry)
    # Helpers
    #Helps to 
    def _find_node(self, key: str):
        node = self.root
        for char in key.lower():
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _collect_entries(self, node: TrieNode) -> list[dict]:
        """DFS in child-insertion order (children dict preserves insertion order
        in Python 3.7+, and chars are inserted in the order words arrive, so a
        pre-sort of keys before building the Trie guarantees strict A-Z output).
        Traverse children sorted by character for guaranteed alphabetical order."""
        results = []
        if node.is_end:
            results.extend(node.entries)
        for char in sorted(node.children.keys()):   # <-- alphabetical DFS
            results.extend(self._collect_entries(node.children[char]))
        return results

    # -------- Core search --------
    def search(self, key: str) -> list[dict]:
        """Return all entries stored under an exact key, or [] if not found."""
        node = self._find_node(key)
        if node and node.is_end:
            return node.entries
        return []

    def starts_with(self, prefix: str) -> list[dict]:
        """Return all entries whose key starts with the given prefix."""
        node = self._find_node(prefix)
        if node is None:
            return []
        return self._collect_entries(node)

    # -------- Alphabetical retrieval --------
    def get_sorted_entries(self) -> list[dict]:
        """
        Return every stored entry in alphabetical order of their key.
        Mirrors HashMap.get_sorted_entries() so both can be swapped in search.py.
        """
        return self._collect_entries(self.root)

    # -------- Stats --------
    def stats(self) -> dict:
        node_count = self._count_nodes(self.root)
        return {
            "unique_keys": self._size,
            "total_nodes": node_count,
        }

    def _count_nodes(self, node: TrieNode) -> int:
        count = 1
        for child in node.children.values():
            count += self._count_nodes(child)
        return count
