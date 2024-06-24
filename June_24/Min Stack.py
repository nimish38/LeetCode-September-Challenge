class MinStack:
    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.st.append((val, val))
        else:
            self.st.append((val, min(val, self.st[-1][1])))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())   #// return 0
print(minStack.getMin()) #// return -2