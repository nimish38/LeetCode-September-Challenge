import random
class RandomizedSet:
    def __init__(self):
        self.list = []
        self.dict = {}
        self.cnt = -1

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.list.append(val)
        self.cnt += 1
        self.dict[val] = self.cnt
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val]
            last_element = self.list[-1]
            self.list[index], self.dict[last_element] = last_element, index
            self.list.pop()
            self.cnt -= 1
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)

x = RandomizedSet()
print(x.insert(1))
print(x.insert(1))
print(x.insert(3))
print(x.remove(2))
print(x.remove(1))
print(x.insert(2))
print(x.getRandom())
print(x.getRandom())
