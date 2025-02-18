class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        for val in self.map:
            if val[0] == key:
                val[1] = value
                return
        self.map.append([key, value])

    def get(self, key: int) -> int:
        for val in self.map:
            if val[0] == key:
                return val[1]
        return -1

    def remove(self, key: int) -> None:
        for i, val in enumerate(self.map):
            if val[0] == key:
               del self.map[i]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)