class LRUCache:

    def __init__(self, capacity: int):
        self.map, self.st, self.cap = {}, [], capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        for i in range(len(self.st)):
            if self.st[i] == key:
                del self.st[i]
                break
            self.st.append(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            self.st.append(key)

        elif len(self.map) == self.cap:
            del self.map[self.st[0]]
            del self.st[0]
            self.map[key] = value
            self.st.append(key)
            