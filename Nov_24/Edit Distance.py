class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n, memo = len(word1), len(word2), []
        for _ in range(m + 1):
            memo.append([-1] * (n + 1))
        #
        # def solve(i, j):
        #     if i >= m or j >= n:
        #         return (m - i) + (n - j)
        #     if memo[i][j] == -1:
        #         if word1[i] == word2[j]:
        #             return solve(i + 1, j + 1)
        #         add = 1 + solve(i, j + 1)
        #         delete = 1 + solve(i + 1, j)
        #         replace = 1 + solve(1 + i, j + 1)
        #         memo[i][j] = min(add, delete, replace)
        #     return memo[i][j]

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m or j == n:
                    memo[i][j] = (m - i) + (n - j)
                elif word1[i] == word2[j]:
                    memo[i][j] = memo[i + 1][j + 1]
                else:
                    add = 1 + memo[i][j + 1]
                    delete = 1 + memo[i + 1][j]
                    replace = 1 + memo[1 + i][j + 1]
                    memo[i][j] = min(add, delete, replace)
        return memo[0][0]

print(Solution().minDistance(word1 = "intention", word2 = "execution"))