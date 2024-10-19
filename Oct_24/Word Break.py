class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n, words = len(s), {}
        for ele in wordDict:
            words[ele] = 1

        def solve(ind):
            if ind >= n or s in words:
                return True
            for i in range(1, n):
                if s[ind: ind + i] in words and solve(ind + i):
                    return True
            return False

        return solve(0)

print(Solution().wordBreak(s = "catsandog", wordDict = ["cats","og","sand","and","cat"]))