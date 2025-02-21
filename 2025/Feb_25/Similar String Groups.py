from collections import defaultdict


class Solution:
    def numSimilarGroups(self, strs) -> int:
        def isSimilar(s1, s2):
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    pos = s2.index(s1[i])
                    s2[i], s2[pos] = s2[pos], s2[i]
                    if s1 != s2:
                        return False
                    return True
            return True

        groups, strs, vis = defaultdict(list), map(list, strs), [False]*len(strs)
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if isSimilar(list(strs[i]), list(strs[j])):
                    groups[i].append(j)
                    groups[j].append(i)

        st, cnt, i = [], 0, 0
        while i < len(strs):
            if not vis[i]:
                vis[i] = True
                cnt += 1
                for j in groups[i]:
                    if not vis[j]:
                        vis[j] = True
            i += 1
        return cnt


print(Solution().numSimilarGroups(strs = ["tars","rats","arts","star"]))