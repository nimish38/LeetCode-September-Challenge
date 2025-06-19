class Solution(object):
    def minExtraChar(self, s, dictionary):
        dictionary, n = {word: 1 for word in dictionary}, len(s)
        memo = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            memo[i] = 1 + memo[i + 1]
            curr = ''
            for j in range(i, n):
                curr += s[j]
                if curr in dictionary:
                    memo[i] = min(memo[i], memo[j + 1])
        return memo[0]


print(Solution().minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"]))