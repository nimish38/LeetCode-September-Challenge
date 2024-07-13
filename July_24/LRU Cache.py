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
        i, found = 0, False
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                del self.cache[i]
                found = True
                break
        if i == self.capacity - 1 and not found and self.cache:
            del self.cache[0]
        self.cache.append((key, value))


lRUCache = LRUCache(2)
print(lRUCache.get(2))
lRUCache.put(2, 6)
print(lRUCache.get(1))
lRUCache.put(1, 5)
lRUCache.put(1, 2)
print(lRUCache.get(1))
print(lRUCache.get(2))