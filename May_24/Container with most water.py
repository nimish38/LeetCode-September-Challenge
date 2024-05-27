class Solution:
    def maxArea(self, height):
        i, j, area = 0, len(height) - 1, 0
        while i < j:
            curr = min(height[i], height[j]) * (j - i)
            if curr > area:
                area = curr

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area

print(Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]))