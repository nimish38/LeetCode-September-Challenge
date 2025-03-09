class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        cnt, curr, currmax = 0, 0, -1
        for val in nums:
            currmax = max(currmax, val)
            if left <= currmax <= right:
                if left <= val <= right:
                    curr += 1
                else:
                    cnt += (curr * (curr + 1)) // 2
                    cnt += 1
                    curr = 0
            else:
                cnt += (curr * (curr + 1)) // 2
                curr, currmax = 0, -1
        cnt += (curr * (curr + 1)) // 2
        return cnt


print(Solution().numSubarrayBoundedMax(nums = [2,9,2,5,6], left = 2, right = 8))