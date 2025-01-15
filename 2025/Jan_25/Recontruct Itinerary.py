from collections import defaultdict
import bisect


class Solution:
    def findItinerary(self, tickets):
        airports, target = defaultdict(list), len(tickets) + 1
        for travel in tickets:
            a, b = travel[0], travel[1]
            bisect.insort(airports[a], b)

        def solve(src, route):
            if len(route) == target - 1:
                route.append(src)
                return route

            for i in range(len(airports[src])):
                val = airports[src][i]
                route.append(src)
                if val != '#':
                    airports[src][i] = '#'
                    travell = solve(val, route)
                    if travell:
                        return travell
                    else:
                        airports[src][i] = val
            return []

        return solve('JFK', [])


print(Solution().findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))