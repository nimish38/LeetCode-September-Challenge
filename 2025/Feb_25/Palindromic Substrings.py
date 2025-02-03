class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt, n, memo = 0, len(s), []
        for _ in range(n):
            memo.append([-2] * n)

        def check(a, b):
            if a > b:
                return True
            if memo[a][b] == -1:
                if s[a] == s[b]:
                    memo[a][b] = check(a + 1, b - 1)
                else:
                    memo[a][b] = False
            return memo[a][b]

        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    cnt += 1
        return cnt


print(Solution().countSubstrings(s = "aaa"))