class Solution(object):
    def splitArray(self, nums, k):
        l, r, best = float('-inf'), 0, -1
        for num in nums:
            if num > l:
                l = num
            r += num

        def checkSplitting(val):
            i, curr, grp = 0, 0, 1
            while i < len(nums) and grp <= k:
                if curr + nums[i] <= val:
                    curr += nums[i]
                else:
                    curr = nums[i]
                    grp += 1
                i += 1
            return grp <= k

        while l <= r:
            mid = ((r - l) // 2) + l
            if checkSplitting(mid):
                best, r = mid, mid - 1
            else:
                l = mid + 1
        return best

print(Solution().splitArray(nums = [1,2,3,4,5], k = 2))