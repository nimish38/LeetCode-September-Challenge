class DSU:
    def __init__(self, n):
        self.parent, self.rank = [], [0] * n
        for _ in range(n):
            self.parent.append(_)

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_par, y_par = self.find(x), self.find(y)
        if x_par != y_par:
            if self.rank[y_par] > self.rank[x_par]:
                self.parent[x_par] = y_par
            else:
                self.parent[y_par] = x_par
                if self.rank[x_par] == self.rank[y_par]:
                    self.rank[x_par] += 1

class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key = lambda x: x[2])

        def Kruskal(take, skip):
            wt, dsu = 0, DSU(n)
            if take != -1:
                dsu.union(edges[take][0], edges[take][1])
                wt += edges[take][2]

            for ind in range(len(edges)):
                if ind == skip:
                    continue
                u, v, w, i = edges[ind]
                if dsu.find(u) != dsu.find(v):
                    dsu.union(u,v)
                    wt += w

            par = dsu.find(0)
            for r in range(1, n):
                if dsu.find(r) != par:
                    return float('inf')
            return wt

        MST_wt, critical, pseudo = Kruskal(-1, -1), [], []
        for i in range(len(edges)):
            if Kruskal(-1, i)  > MST_wt:
                critical.append(edges[i][3])
            elif Kruskal(i, - 1) == MST_wt:
                pseudo.append(edges[i][3])
        return [critical, pseudo]

print(Solution().findCriticalAndPseudoCriticalEdges(n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]))