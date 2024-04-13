class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str):
        m, n = len(text1), len(text2)
        memo = []
        for i in range(m + 1):
            temp = []
            for j in range(n + 1):
                if i == 0 or j == 0:
                    temp.append(0)
                else:
                    temp.append(-1)
            memo.append(temp)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i][j - 1], memo[i - 1][j])
        # print(memo)
        return memo[m][n]


print(Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace"))