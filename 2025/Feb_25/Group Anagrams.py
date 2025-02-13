from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for word in strs:
            sortedWord = sorted(word)
            res[sortedWord].append(word)
        return list(res.values())

