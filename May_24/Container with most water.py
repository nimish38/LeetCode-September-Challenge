class Solution:
    def maxArea(self, height):
        i, j, area = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                curr = height[i] * (j - i)
                if curr > area:
                    area = curr
                i += 1
            else:
                curr = height[j] * (j - i)
                if curr > area:
                    area = curr
                j -= 1
        return area

print(Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]))