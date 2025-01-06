from collections import Counter
class Solution:
    def maxOperations(self, nums, k):
        res, d = 0, Counter(nums)

        for val1, val1Cnt in d.items():
            val2 = k - val1
            # to get rid of duplicates consider only pairs where val1 >= val2
            if val1 < val2 or val2 not in d: continue
            res += min(val1Cnt, d[val2]) if val1 != val2 else val1Cnt // 2

        return res

print(Solution().maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))
