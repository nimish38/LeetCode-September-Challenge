class Solution(object):
    def countSubstrings(self, s):
        self.cnt, n = 0, len(s)
        def expand(i, j):
            while 0 <= i and j < n and s[i] == s[j]:
                self.cnt += 1
                i -= 1
                j += 1
        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return self.cnt

print(Solution().countSubstrings('aaa'))