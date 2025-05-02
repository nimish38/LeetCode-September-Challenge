class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDict, n = {key : 1 for key in wordDict}, len(s)
        memo = [-1] * n
        def solve(ind):
            if ind >= len(s):
                return True
            if memo[ind] == -1:
                for i in range(1, n - ind + 1):
                    val = s[ind: ind + i]
                    if val in wordDict and solve(i + ind):
                        memo[ind] = True
                        break
                if memo[ind] == -1:
                    memo[ind] =False
            return memo[ind]

        return solve(0)

print(Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))