class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str):
        m, n = len(text1), len(text2)
        memo = []
        for _ in range(m):
            memo.append([-1] * n)

        def dpLcs(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + dpLcs(i + 1, j + 1)
            if memo[i][j] == -1:
                memo[i][j] = max(dpLcs(i + 1, j), dpLcs(i, j + 1))
            return memo[i][j]
        return dpLcs(0, 0)

print(Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace"))