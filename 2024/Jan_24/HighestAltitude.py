class Solution:
    def largestAltitude(self, gain):
        highest = max(0, gain[0])
        for i in range(1, len(gain)):
            gain[i] += gain[i-1]
            if gain[i] > highest:
                highest = gain[i]
        return highest

print(Solution().largestAltitude([-5,1,5,0,-7]))