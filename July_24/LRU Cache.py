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


    def put(self, key: int, value: int) -> None:
        

lRUCache = LRUCache(2)
print(lRUCache.get(2))
lRUCache.put(2, 6)
print(lRUCache.get(1))
lRUCache.put(1, 5)
lRUCache.put(1, 2)
print(lRUCache.get(1))
print(lRUCache.get(2))