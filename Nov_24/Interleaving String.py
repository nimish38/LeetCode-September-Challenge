class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o, memo = len(s1), len(s2), len(s3), []
        if m + n != o:
            return False
        for _ in range(m+1):
            l = []
            for x in range(n+1):
                l.append([-1] * (o+1))
            memo.append(l)

        def solve(i, j, k):
            if i == m and j == n and k == o:
                return True
            if memo[i][j][k] == -1:
                first, second = False, False
                if j < n and s3[k] == s2[j]:
                    second = solve(i, j + 1, k + 1)
                if i < m and  s3[k] == s1[i]:
                    first = solve(i + 1, j, k + 1)
                memo[i][j][k] =  first or second
            return memo[i][j][k]

        return solve(0, 0, 0)

print(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
