class LRUCache:
    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                val = self.cache[i][1]
                del self.cache[i]
                self.cache.append((key, val))
                return val
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                del self.cache[i]
                break
        if i == self.capacity:
            del self.cache[0]
        self.cache.append((key, value))

