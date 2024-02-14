class Solution:
    def maxArea(self, height) -> int:
        area = -1
        i, j = 0, len(height) - 1
        while i < j:
            # print(i, j)
            curArea = (j - i) * min(height[i], height[j])
            if curArea > area:
                area = curArea
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))