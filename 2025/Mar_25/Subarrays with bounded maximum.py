class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        cnt, curr, currmax, out = 0, 0, -1, 0
        for val in nums:
            currmax = max(currmax, val)
            if left <= currmax <= right:
                if left <= val <= right:
                    cnt -= (out * (out + 1)) // 2
                    out = 0
                else:
                    out += 1
                curr += 1
            else:
                cnt += (curr * (curr + 1)) // 2
                cnt -= (out * (out + 1)) // 2
                curr, currmax, out = 0, -1, 0
        cnt += (curr * (curr + 1)) // 2
        cnt -= (out * (out + 1)) // 2
        return cnt


print(Solution().numSubarrayBoundedMax(nums = [2,9,2,5,6], left = 2, right = 8))