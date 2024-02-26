# got from leetcode discuss
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        start = 0
        end = 0
        product = 1
        while(end < n):
            product *= nums[end]
            while( start < n and product >= k):
                product /= nums[start]
                start+=1
            if product < k: count += end - start + 1
            end+=1
        return count