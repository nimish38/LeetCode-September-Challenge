class Solution:
    def largestAltitude(self, gain):
        highest = curr = 0
        for height in gain:
            curr += height
            if curr > highest:
                highest = curr
        return highest

print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))