class MinStack(object):

    def __init__(self):
        self.mst, self.min = [], float('inf')

    def push(self, val):
        if self.min > val:
            self.min = val
        self.mst.append((val, self.min))

    def pop(self):
        popped = self.mst.pop()[1]
        if popped == self.min:
            if self.mst:
                self.min = self.mst[-1][1]
            else:
                self.min = float('inf')

    def top(self):
        return self.mst[-1][0]

    def getMin(self):
        return self.mst[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()