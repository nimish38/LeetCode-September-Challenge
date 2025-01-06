from collections import defaultdict

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def checkdigits(num):
            arr = defaultdict(int)
            while num > 0:
                arr[num % 10] += 1
                num //= 10
            return arr

        val, given = 1, checkdigits(n)
        for _ in range(31):
            if checkdigits(2 ** _) == given:
                return True
        return False


print(Solution().reorderedPowerOf2(2041))