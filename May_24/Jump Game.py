class Solution:
    def canJump(self, nums):
        stack = [(0, nums[0])]
        while stack:
            ind, num = stack.pop()
            for i in range(ind + 1, ind + num):
                if i >= len(nums):
                    return True
                stack.append((i, nums[i]))
        if stack:
            return True
        return False

    

