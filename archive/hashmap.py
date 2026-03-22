class HashMap:
    initial_capacity = 1024
    load_factor = 0.7

    def __init__(self):
        self._capacity = self.initial_capacity
        self._size = 0
        self._buckets = [None] * self._capacity

    # hash function
    def _hash(self, key: str) -> int:
        base = 31
        h = 0
        power = 1
        for c in key:
            h = (h + ord(c) * power) % self._capacity
            power = (power * base) % self._capacity
        return h

    # core functions
    def _probe(self, key: str) -> tuple:
        index = self._hash(key)

        for _ in range(self._capacity):
            cell = self._buckets[index]

            if cell is None:
                return index, False # empty cell, no key

            if cell[0] == key:
                return index, True # key found

            index = (index + 1) % self._capacity # next cell

        return index, False # table full

    def insert(self, key: str, entry: dict):
        if self._size / self._capacity >= self.load_factor:
            self._resize()

        index, found = self._probe(key)

        if found:
            self._buckets[index][1].append(entry)
        else:
            self._buckets[index] = [key, [entry]]
            self._size += 1

    def get(self, key: str) -> list:
        index, found = self._probe(key)
        if found:
            return self._buckets[index][1]
        return []

    # entries
    def get_all_entries(self) -> list:
        all_entries = []
        for bucket in self._buckets:
            if bucket is not None:
                key, entries = bucket
                all_entries.extend(entries)
        return all_entries

    # sort entries
    def get_sorted_entries(self, sort_key="match_count", reverse=True) -> list:
        all_entries = self.get_all_entries()
        return sorted(all_entries, key=lambda x: x.get(sort_key, 0), reverse=reverse)

    # misc
    def _resize(self):
        old_buckets = self._buckets
        self._capacity = self._capacity * 2
        self._size = 0
        self._buckets = [None] * self._capacity

        for cell in old_buckets:
            if cell is None:
                continue
            key, entries = cell
            for entry in entries:
                self.insert(key, entry)

    def stats(self) -> dict:
        occupied = sum(1 for c in self._buckets if c is not None)
        return {
            "capacity": self._capacity,
            "live_keys": self._size,
            "occupied": occupied,
            "load_factor": round(occupied / self._capacity, 4),
        }