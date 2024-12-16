class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        i, j, zero, one, score = 0, n - 1, 0, 0, [0] * n

        while i < n:
            if s[i] == '0':
                zero += 1
            if s[j] == '1':
                one += 1
            score[i], score[j] = score[i] + zero, score[j] + one
            i += 1
            j -= 1

        if zero == 0 or one == 0:
            return max(score) - 1
        return max(score)

print(Solution().maxScore(s = "111"))