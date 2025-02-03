class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt, n = len(s), len(s)
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                val = s[i : i + length]
                if val == val[::-1]:
                    cnt += 1
        return cnt


print(Solution().countSubstrings(s = "aaa"))