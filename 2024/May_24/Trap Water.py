class Solution:
    def trap(self, height):
        n = len(height)
        left_max, right_max = [0] * n, [0] * n

        # build left max
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # build right max in reverse
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # find trapped water
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water

print(Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
