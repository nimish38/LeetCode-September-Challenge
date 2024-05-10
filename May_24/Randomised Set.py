import random
class RandomizedSet:

    def __init__(self):
        self.myset = {}

    def insert(self, val: int) -> bool:
        if val in self.myset:
            return False
        self.myset[val] = val
        return True

    def remove(self, val: int) -> bool:
        if val in self.myset:
            self.myset.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.myset.values()))

x = RandomizedSet()
print(x.insert(1))
print(x.insert(1))
print(x.insert(3))
print(x.remove(2))
print(x.remove(1))
print(x.insert(2))
print(x.getRandom())
print(x.getRandom())
