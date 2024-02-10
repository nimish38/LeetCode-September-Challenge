class Solution:
    def increasingTriplet(self, nums):
        minOne = float('inf')
        minTwo = float("Inf")
        for num in nums:
            if num < minOne:
                minOne = num
            elif num > minOne and num < minTwo:
                minTwo = num
            elif num > minTwo:
                return True
        return False


a = Solution()
print(a.increasingTriplet([0,4,2,1,0,-1,-3]))