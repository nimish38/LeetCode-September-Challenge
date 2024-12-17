class Solution:
    def maxScore(self, s: str) -> int:
        n, score = len(s), 0
        for i in range(n - 1):
            zero, one = 0, 0
            for j in range(i + 1):
                if s[j] == '0':
                    zero += 1
            for j in range(i + 1, n):
                if s[j] == '1':
                    one += 1
            score = max(score, one + zero)
        return score

print(Solution().maxScore(s = "111"))