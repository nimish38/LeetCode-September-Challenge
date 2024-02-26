class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # get only unique elements
        curr = 1
        nums = list(set(nums))
        # sort the list
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 1:
                continue
            # if number is not equal to curr, return the answer    
            if nums[i] != curr:
                return curr
            curr += 1
        return curr    