class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()
        while n != 1:
            if n in vis:
                return False
            vis.add(n)
            n = sum([int(i)**2 for i in str(n)])
        return True

print(Solution().isHappy(n = 7))
