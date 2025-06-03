from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        adj, n, st, res  = defaultdict(list), len(tickets) + 1, ['JFK'], []
        for f, t in tickets:
            adj[f].append(t)
        for key in adj:
            adj[key].sort(reverse=True)

        while st:
            city = st[-1]
            if city in adj and adj[city]:
                st.append(adj[city].pop())
            else:
                # this gets all cities that have 0 in degree one by one
                res.append(st.pop())
        return res[::-1]

print(Solution().findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))