import bisect
class Solution:
    def lengthOfLIS(self, nums) -> int:
        n, arr = len(nums), []

        for num in nums:
            ind = bisect.bisect_left(arr, num)
            if ind == len(arr):
                arr.append(num)
            else:
                arr[ind] = num
        return len(arr)

print(Solution().lengthOfLIS(nums = [0,1,0,3,2,3]))