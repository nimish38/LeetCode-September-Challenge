class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        trie = {}
        for word in wordDict:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['*'] = True

        def solve(i, cur):
            if i >= len(s):
                if '*' in cur:
                    return True
                return False
            if s[i] not in cur:
                return False
            cur, new_explore = cur[s[i]], False
            if '*' in cur:
                new_explore = solve(i + 1, trie)
            return solve(i + 1, cur) or new_explore

        return solve(0, trie)

print(Solution().wordBreak(s = "aaaaaaa", wordDict = ["aaaa","aa"]))