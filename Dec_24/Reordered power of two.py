from collections import defaultdict

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def checkdigits(num):
            arr = defaultdict(0)
            while num > 0:
                arr[num % 10] += 1
                num //= 10
            return arr
        
print(Solution().reorderedPowerOf2(2041))