class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if m + n != o:
            return False

        def solve(i, j, k):
            if i == m and j == n and k == o:
                return True
            if i == m or j == n or k == o:
                return False
            first, second = False, False
            if s3[k] == s2[j]:
                second = solve(i, j + 1, k + 1)
            if s3[k] == s1[i]:
                first = solve(i + 1, j, k + 1)
            return first or second

        return solve(0, 0, 0)


