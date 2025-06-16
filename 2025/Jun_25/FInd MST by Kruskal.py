class Solution:
    def spanningTree(self, V, adj) -> int:
        temp, adj = adj, []
        for i in range(V):
            for v, w in temp[i]:
                adj.append([i, v, w])
        adj.sort(key= lambda x:x[2])
        parent, rank, cost = [], [0] * V, 0
        for _ in range(V):
            parent.append(_)

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x_par, y_par = find(x), find(y)
            if x_par != y_par:
                if rank[x_par] > rank[y_par]:
                    parent[y_par] = x_par
                else:
                    parent[x_par] = y_par
                    if rank[x_par] == rank[y_par]:
                        rank[y_par] += 1

        for u, v, w in adj:
            if find(u) != find(v):
                union(u, v)
                cost += w
        return cost


print(Solution().spanningTree(3, [[[1, 5], [2, 1]],[[0, 5], [2, 3]],[[1, 3], [0, 1]]]))
