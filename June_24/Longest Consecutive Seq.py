class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        val, res = {}, -1
        for num in set(nums):
            lcont, rcont = val.get(num - 1, 0), val.get(num + 1, 0)
            curr = lcont + rcont + 1
            val[num - lcont] = val[num + rcont] = curr
            res = max(res, curr)
        return res

print(Solution().longestConsecutive(nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))