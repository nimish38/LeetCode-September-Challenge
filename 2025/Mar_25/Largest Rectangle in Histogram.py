class Solution(object):
    def largestRectangleArea(self, heights):
        st, best, n = [], 0, len(heights)
        for i in range(n):
            val = heights[i]
            while st and val < heights[st[-1]]:
                curr = heights[st.pop()]
                if not st:
                    pse = -1
                else:
                    pse = st[-1]
                best = max(best, curr * (i - pse - 1))
            st.append(i)

        while st:
            curr = heights[st.pop()]
            if not st:
                pse = -1
            else:
                pse = st[-1]
            best = max(best, curr * (n - pse - 1))

        return best

print(Solution().largestRectangleArea(heights = [2,1,5,6,2,3]))