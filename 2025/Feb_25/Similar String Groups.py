from collections import defaultdict


class Solution:
    def numSimilarGroups(self, strs) -> int:
        def isSimilar(s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
            return diff == 2 or diff == 0
        groups, strs, vis = defaultdict(list), list(map(list, strs)), [False]*len(strs)
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if isSimilar(list(strs[i]), list(strs[j])):
                    groups[i].append(j)
                    groups[j].append(i)
        cnt, i = 0, 0
        def dfs(ind):
            if not vis[ind]:
                vis[ind] = True
                for j in groups[ind]:
                    if not vis[j]:
                        dfs(j)
        while i < len(strs):
            if not vis[i]:
                dfs(i)
                cnt += 1
            i += 1
        return cnt


print(Solution().numSimilarGroups(strs = ["tars","rats","arts","star"]))