class DLL:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.map, self.cap = {}, capacity
        self.head, self.tail = DLL('a'), DLL('z')

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        add, val = self.map[key]
        self.remove_node(add)
        self.push_back(key, val)

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            add, val = self.map[key]
            self.remove_node(add)
            self.push_back(key, val)

        elif len(self.map) == self.cap:
            self.remove_node(self.head.next)
        self.push_back(key, value)


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))
lru.put(3, 3)
print(lru.get(2))
lru.put(4,4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))
