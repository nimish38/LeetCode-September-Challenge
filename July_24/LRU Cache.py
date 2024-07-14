class Dll:
    def __init__(self,key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Dll(-1, -1)
        self.tail = Dll(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            val, node = self.cache[key]
            self.remove_node(node)
            self.push_back(key, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key][1]
            self.remove_node(node)
            self.push_back(key, value)
        else:
            if len(self.cache) == self.capacity:
                lru_node = self.head.next
                self.remove_node(lru_node)
            self.push_back(key, value)


lRUCache = LRUCache(2)
print(lRUCache.get(2))
lRUCache.put(2, 6)
print(lRUCache.get(1))
lRUCache.put(1, 5)
lRUCache.put(1, 2)
print(lRUCache.get(1))
print(lRUCache.get(2))