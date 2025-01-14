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
        if len(self.st) == self.cap:
            val = self.st[0]
            del self.st[0]
            del self.dic[val]
            self.st.append(key)
            self.dic[key] = value
        else:
            if key in self.dic:
                self.st.remove(key)
            self.dic[key] = value
            self.st.append(key)


obj = LRUCache(2)
print(obj.put(1, 1))
print(obj.put(2, 2))
print(obj.get(1))
print(obj.put(3, 3))
print(obj.get(2))
print(obj.put(4, 4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

