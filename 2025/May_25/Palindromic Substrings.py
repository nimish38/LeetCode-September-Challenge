class Solution:
    def countSubstrings(self, s: str) -> int:
        n, cnt = len(s), 0

        def expand(i, j):
            val, left, right = 1, i, j
            while left > 0 and right < n - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
                val += 1
            return val

        for ind in range(n):
            odd, even = expand(ind, ind), 0
            if ind < n - 1 and s[ind] == s[ind + 1]:
                even = expand(ind, ind + 1)
            cnt += odd + even
        return cnt

print(Solution().countSubstrings(s = "aaa"))