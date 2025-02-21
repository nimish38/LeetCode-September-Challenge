from collections import defaultdict


class Solution:
    def numSimilarGroups(self, strs) -> int:
        def isSimilar(s1, s2):
            k, n = 2, len(s1)
            def getPos(st, c):
                for i in range(n):
                    if st[i] == c:
                        return i
            while k > 0:
                for i in range(n):
                    if s1[i] != s2[i]:
                        pos = getPos(s2, s1[i])
                        s2[i], s2[pos] = s2[pos], s2[i]
                        k -= 1
                        break
                if s1 == s2:
                    return True
            return False

        groups = defaultdict(set)
        for i in range(len(strs)):
            for j in range(len(strs)):
                if isSimilar(strs[i], strs[j]):
                    groups[strs[i]].add(strs[j])