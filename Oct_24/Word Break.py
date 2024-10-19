class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)

        def solve(ind):
            if ind >= n or s in wordDict:
                return True
            for i in range(1, n):
                if s[ind: ind + i] in wordDict and solve(ind + i):
                    return True
            return False

        return solve(0)