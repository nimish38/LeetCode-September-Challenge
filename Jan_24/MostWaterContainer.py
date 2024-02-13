class Solution:
    def maxArea(self, height) -> int:
        area = -1
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                curArea = (j - i) * min(height[i], height[j])
                if curArea > area:
                    area = curArea
        return area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))