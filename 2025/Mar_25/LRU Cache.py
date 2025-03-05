class DLL:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.map, self.cap = {}, capacity
        self.head, self.tail = DLL('a'), DLL('z')
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        add, val = self.map[key]
        self.remove_node(add)
        self.push_back(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            add, val = self.map[key]
            self.remove_node(add)
        elif len(self.map) == self.cap:
            self.remove_node(self.head.next)
        self.push_back(key, value)

    def remove_node(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
        del self.map[node.key]

    def push_back(self, k, v):
        new_node = DLL(k)
        last = self.tail.prev
        last.next, new_node.prev = new_node, last
        new_node.next, self.tail.prev = self.tail, new_node
        self.map[k] = (new_node, v)


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
