import bisect


class Solution:
    def lengthOfLIS(self, nums) -> int:
        n, arr = len(nums), []
        for i in range(n):
            val = bisect.bisect_left(arr, nums[i])
            if val == len(arr):
                arr.append(nums[i])
            else:
                arr[val] = nums[i]
        return len(arr)


print(Solution().lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))