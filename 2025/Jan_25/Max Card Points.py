class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        res = 0
        for i in range(k):
            res += cardPoints[i]
        if len(cardPoints) == k:
            return sum(cardPoints)
        j, best = len(cardPoints) - 1, res
        while k > 0:
            res = res - cardPoints[i] + cardPoints[j]
            best = max(res, best)
            i -= 1
            j -= 1
            k -= 1
        return best


print(Solution().maxScore(cardPoints = [2,2,2], k = 2))