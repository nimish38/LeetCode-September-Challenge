class Solution:
    def trap(self, height) -> int:
        n, water = len(height), 0
        l, r, max_left, max_right = 0, n - 1, 0, 0
        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                water += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                water += max_right - height[r]
                r -= 1
        return water


print(Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))