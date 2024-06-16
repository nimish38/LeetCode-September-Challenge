class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        val, res = {}, -1
        for num in nums:
            if num in val:
                continue
            lcont, rcont = 0, 0
            if num - 1 in val:
                lcont = val[num - 1]
            if num + 1 in val:
                rcont = val[num + 1]
            val[num] = lcont + rcont + 1
            if lcont:
                while lcont > 0:
                    val[num - lcont] = val[num]
                    lcont -= 1
            if rcont:
                while rcont:
                    val[num + rcont] = val[num]
                    rcont -= 1
            res = max(res, val[num])
        return res

print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))