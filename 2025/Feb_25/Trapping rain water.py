class Solution:
    def trap(self, height) -> int:
        n, water = len(height), 0
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i - 1])
            right[n - 1 - i] = max(right[n - i], height[n - i])
        for i in range(n):
            water += max(min(left[i], right[i]) - height[i], 0)
        return water


print(Solution().trap(height = [4,2,0,3,2,5]))