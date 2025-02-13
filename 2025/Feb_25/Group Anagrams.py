from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            res[sortedWord].append(word)
        return list(res.values())


print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))

