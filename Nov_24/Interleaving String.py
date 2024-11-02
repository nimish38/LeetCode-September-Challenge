class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if m + n != o:
            return False

        def solve(i, j, k):
            if i == m and j == n and k == o:
                return True
            first, second = False, False
            if j < n and s3[k] == s2[j]:
                second = solve(i, j + 1, k + 1)
            if i < m and  s3[k] == s1[i]:
                first = solve(i + 1, j, k + 1)
            return first or second

        return solve(0, 0, 0)

print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
