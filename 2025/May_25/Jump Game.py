class Solution:
    def canJump(self, nums) -> bool:
        n, i, maxReach = len(nums) - 1, 0, 0
        while i < n and maxReach < n:
            if maxReach < i:
                return False
            maxReach = max(maxReach, i + nums[i])
            i += 1
        return maxReach >= n

print(Solution().canJump(nums = [3,2,1,0,4]))