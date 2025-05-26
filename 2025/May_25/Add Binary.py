class Solution(object):
    def addBinary(self, a, b):
        a, b = int(a, 2), int(b, 2)
        return bin(a + b)[2:]

print(Solution().addBinary("110010", "10111"))