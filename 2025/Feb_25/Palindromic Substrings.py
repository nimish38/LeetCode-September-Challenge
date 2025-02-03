class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt, n, memo = 0, len(s), []
        for _ in range(n + 1):
            memo.append([False] * (n + 1))

        for length in range(1, n + 1):
            i = 0
            while i + length - 1 < n:
                j = i + length - 1
                if i == j:
                    memo[i][j] = True
                elif i + 1 == j:
                    memo[i][j] = s[i] == s[j]
                else:
                    memo[i][j] = (s[i] == s[j]) and memo[i + 1][j - 1]
                if memo[i][j]:
                    cnt += 1
                i += 1
        return cnt


print(Solution().countSubstrings(s = "abc"))