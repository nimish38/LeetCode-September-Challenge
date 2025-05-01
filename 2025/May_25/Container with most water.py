class Solution:
    def maxArea(self, height) -> int:
        i, j, best = 0, len(height) - 1, 0
        while i < j:
            curr = min(height[i], height[j])
            best = max(curr * (j - i), best)
            while i < j and height[i] <= curr:
                i+=1
            while i < j and height[j] <= curr:
                j-=1
        return best

print(Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]))