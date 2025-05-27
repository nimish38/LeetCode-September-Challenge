class Solution(object):
    def mergeAlternately(self, word1, word2):
        i, j, res, flag = 0, 0, '', True
        while i < len(word1) and j < len(word2):
                res += word1[i]
                i += 1
                res += word2[j]
                j += 1
        if i < len(word1):
            res += word1[i : ]
        if j < len(word2):
            res += word2[j : ]