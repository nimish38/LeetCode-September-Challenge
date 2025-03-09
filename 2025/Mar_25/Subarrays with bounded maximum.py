class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        cnt, curr = 0, 0
        for val in nums:
            if left <= val <= right:
                curr += 1
            else:
                cnt += (curr * (curr + 1)) // 2
                curr = 0
        cnt += (curr * (curr + 1)) // 2
        return cnt

