class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt, n = len(s), len(s)
        for length in range(1, n):
            for i in range(n - length):
                val = s[i : i + length]
                if val == val[::-1]:
                    cnt += 1
        return cnt