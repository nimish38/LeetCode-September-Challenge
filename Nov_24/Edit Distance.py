class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def solve(i, j):
            if i >= m or j >= n:
                return (m - i) + (n - j)
            if word1[i] == word2[j]:
                return solve(i + 1, j + 1)
            add = 1 + solve(i, j + 1)
            delete = 1 + solve(i + 1, j)
            replace = 1 + solve(1 + i, j + 1)
            return min(add, delete, replace)

        return solve(0, 0)

print(Solution().minDistance(word1 = "intention", word2 = "execution"))