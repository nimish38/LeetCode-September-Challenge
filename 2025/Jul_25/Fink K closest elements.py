from collections import defaultdict


class Solution(object):
    def findClosestElements(self, arr, k, x):
        cnt, res = defaultdict(list), []
        for num in arr:
            cnt[abs(num - x)].append(num)
        for key in sorted(list(cnt.keys())):
            if len(cnt[key]) > k:
                res.extend(sorted(cnt[key])[: k])
                break
            else:
                res.extend(cnt[key])
                k -= len(cnt[key])
        res.sort()
        return res

print(Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))