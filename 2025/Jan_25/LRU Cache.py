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
        if len(self.st) == self.capacity:
            val = self.st[0]
            del self.st[0]
            del self.dic[val]
            self.st.append(key)
            self.dic[key] = val
        else:
            if key in self.dic:
                self.st.remove(key)
            self.dic[key] = value
            self.st.append(key)
