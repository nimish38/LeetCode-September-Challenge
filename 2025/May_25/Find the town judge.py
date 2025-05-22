class Solution(object):
    def findJudge(self, n, trust):
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1
print(Solution().findJudge(n = 3, trust = [[1,3],[2,3]]))