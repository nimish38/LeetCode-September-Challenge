class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = []
        for _ in range(m):
            memo.append([-1] * n)

        def match(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if memo[i][j] == -1:
                if word1[i] == word2[j]:
                    memo[i][j] = match(i + 1, j + 1)
                else:
                    insert = 1 + match(i, j + 1)
                    delete = 1 + match(i + 1, j)
                    replace = 1 + match(i + 1, j + 1)
                    memo[i][j] = min(insert, delete, replace)
            return memo[i][j]
        return match(0, 0)

print(Solution().minDistance(word1 = "horse", word2 = "ros"))