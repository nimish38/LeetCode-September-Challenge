class Solution:
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        stack = [(0, nums[0])]
        while stack:
            ind, num = stack.pop()
            for i in range(ind + 1, ind + num + 1):
                if i >= len(nums) - 1:
                    return True
                stack.append((i, nums[i]))
        if stack:
            return True
        return False

print(Solution().canJump(nums = [2,0,0]))

