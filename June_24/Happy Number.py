class Solution:
    def isHappy(self, n: int) -> bool:
        val, curr = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}, -1
        while n > 9 and curr != n:
            curr, sum = n, 0
            for char in str(n):
                sum += val[char]
            n = sum

        if n == 1:
            return True
        return False

print(Solution().isHappy(n = 97))
