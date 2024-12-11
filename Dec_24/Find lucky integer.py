from collections import defaultdict
class Solution:
    def findLucky(self, arr) -> int:
        cnt, best = defaultdict(int), -1
        for val in arr:
            cnt[val] += 1
        
        for val in cnt:
            if cnt[val] == val and val > best:
                best = val
        return best                


print(Solution().findLucky(arr = [1,2,2,3,3,3]))