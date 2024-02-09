class Solution:
    def increasingTriplet(self, nums):
        prevIncreasing = False
        for i in range(len(nums) - 2):
            lastIncrement = float('inf')
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if prevIncreasing and nums[j] > lastIncrement:
                        return True
                    prevIncreasing = True
                    lastIncrement = min(lastIncrement, nums[j])
        return False


a = Solution()
print(a.increasingTriplet([1,5,0,4,1,3]))