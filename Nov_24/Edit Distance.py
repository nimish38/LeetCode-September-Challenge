class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n, memo = len(word1), len(word2), []
        for _ in range(m):
            memo.append([-1]*n)

        def solve(i, j):
            if i >= m or j >= n:
                return (m - i) + (n - j)
            if memo[i][j] == -1:
                if word1[i] == word2[j]:
                    return solve(i + 1, j + 1)
                add = 1 + solve(i, j + 1)
                delete = 1 + solve(i + 1, j)
                replace = 1 + solve(1 + i, j + 1)
                memo[i][j] = min(add, delete, replace)
            return memo[i][j]

        return solve(0, 0)

print(Solution().minDistance(word1 = "intention", word2 = "execution"))