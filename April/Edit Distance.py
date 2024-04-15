class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        def match(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return match(i + 1, j + 1)

            insert = 1 + match(i, j + 1)
            delete = 1 + match(i + 1, j)
            replace = 1 + match(i + 1, j + 1)
            return min(insert, delete, replace)
        return match(0, 0)

print(Solution().minDistance(word1 = "horse", word2 = "ros"))