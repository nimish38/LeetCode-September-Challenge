from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        curr, mappings = set(), defaultdict(list)
        for str in strs:
            curr = ''.join(sorted(str))
            mappings[curr].append(str)

        return list(mappings.values())

print(Solution().groupAnagrams(strs = ["a"]))