class LRUCache:

    def __init__(self, capacity: int):
        self.cap, self.st, self.dic = capacity, [], {}

    def get(self, key: int) -> int:
        if key in self.dic:
            self.st.remove(key)
            self.st.append(key)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.st.remove(key)

        elif len(self.st) == self.cap:
            val = self.st[0]
            del self.st[0]
            del self.dic[val]
        self.st.append(key)
        self.dic[key] = value



obj = LRUCache(2)
print(obj.get(2))
print(obj.put(2, 6))
# print(obj.put(2, 2))
print(obj.get(1))
print(obj.put(1, 5))
# print(obj.get(2))
print(obj.put(1, 2))
print(obj.get(1))
print(obj.get(2))
# print(obj.get(4))

