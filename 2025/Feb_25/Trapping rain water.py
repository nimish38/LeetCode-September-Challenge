class Solution:
    def trap(self, height) -> int:
        n, water = len(height), 0
        left, right = [0] * n, [0] * n
        left[0], right[-1] = height[0], height[-1]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
            right[n - 1 - i] = max(right[n - i], height[n - i - 1])
        for i in range(n):
            water += min(left[i], right[i]) - height[i]
        return water


print(Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))