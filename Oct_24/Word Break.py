class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)

        def solve(ind):
            if ind >= n:
                return False
            for i in range(1, n - ind - 1):
                if s[ind: ind + i] in wordDict:
                    if s[ind + i + 1:] in wordDict:
                        return True
                    return solve(ind + i + 1)
            return False

        return solve(o)