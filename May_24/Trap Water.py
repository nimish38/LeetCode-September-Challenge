class Solution:
    def trap(self, height):
        n = len(height)
        left_max, right_max = [], []

        for i in range(1, n - 1):
            left_max.append(max(height[:i]))
            right_max.append(max(height[i:]))

        left_max.insert(0, height[0])
        left_max.append(max(height))

        right_max.insert(0, max(height))
        right_max.append(height[-1])

        water = 0
        for i in range(n):
            cnt = min(left_max[i], right_max[i]) - height[i]
            if cnt > 0:
                water += cnt
        return water

print(Solution().trap(height = [4,2,0,3,2,5]))
