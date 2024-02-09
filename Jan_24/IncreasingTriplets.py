class Solution:
    def increasingTriplet(self, nums):
        prevIncreasing = False
        lastIncreaingMin = float('inf')

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if prevIncreasing and nums[i] > lastIncreaingMin:
                    return True
                prevIncreasing = True
                lastIncreaingMin = min(lastIncreaingMin, nums[i])
        return False

a = Solution()
print(a.increasingTriplet([6,7,1,2]))