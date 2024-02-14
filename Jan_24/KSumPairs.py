class Solution:
    def maxOperations(self, nums, k):
        val, cnt = dict(), 0
        for num in nums:
            diff = k - num
            if diff > 0 and diff in val.keys():
                cnt += 1
                if val[diff] > 1:
                    val[diff] -= 1
                else:
                    del val[diff]
            else:
                if num in val.keys():
                    val[num] += 1
                else:
                    val[num] = 1
        return cnt

print(Solution().maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))
