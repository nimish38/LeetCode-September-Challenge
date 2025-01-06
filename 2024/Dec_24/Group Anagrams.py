class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in anagrams:
                anagrams[sortedWord].append(word)
            else:
                anagrams[sortedWord] = [word]
        res = []
        for val in anagrams:
            res.append(anagrams[val])
        return res


print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))