class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = []
        for _ in range(m + 1):
            memo.append([-1] * (n + 1))

        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0 or j == 0:
                    memo[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    insert = 1 + memo[i][j - 1]
                    delete = 1 + memo[i - 1][j]
                    replace = 1 + memo[i - 1][j - 1]
                    memo[i][j] = min(insert, delete, replace)
        return memo[m][n]


print(Solution().minDistance(word1 = "horse", word2 = "ros"))