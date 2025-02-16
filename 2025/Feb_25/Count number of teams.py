class Solution:
    def numTeams(self, rating) -> int:
        cnt, n = 0, len(rating)
        for j in range(1, n - 1):
            leftsmall, leftlarge, rightsmall, rightlarge = 0, 0, 0, 0
            for i in range(j):
                if rating[i] < rating[j]:
                    leftsmall += 1
                if rating[i] > rating[j]:
                    leftlarge += 1
            
        return cnt


print(Solution().numTeams(rating = [2,5,3,4,1]))

