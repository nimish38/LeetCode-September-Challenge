class Solution:
    def maxScore(self, s: str) -> int:
        n, score, zero, one = len(s), float('-inf'), 0, 0
        for i in range(n - 1):
            if s[i] == '0':
                zero += 1
            if s[i] == '1':
                one += 1
            score = max(score, zero - one)
        if s[-1] == '1':
            one += 1
        return score + one

print(Solution().maxScore(s = "1111"))