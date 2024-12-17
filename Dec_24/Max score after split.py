class Solution:
    def maxScore(self, s: str) -> int:
        n, score, ones, zero, one = len(s), 0, s.count('1'), 0, 0
        for i in range(n - 1):
            if s[i] == '0':
                zero += 1
            if s[i] == '1':
                one += 1
            score = max(score, zero + ones - one)
        return score

print(Solution().maxScore(s = "00111"))