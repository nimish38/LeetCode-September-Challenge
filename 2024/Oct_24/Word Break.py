class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n, words = len(s), {}
        for ele in wordDict:
            words[ele] = 1
        memo = [-1] * (n + 1)

        def solve(ind):
            if ind >= n or s in words:
                return True
            if memo[ind] == -1:
                for i in range(1, n):
                    if s[ind: ind + i] in words and solve(ind + i):
                        memo[ind] = True
                        return True
                memo[ind] = False
            return memo[ind]

        return solve(0)

print(Solution().wordBreak(s = "catsandog", wordDict = ["cats","og","sand","and","cat"]))