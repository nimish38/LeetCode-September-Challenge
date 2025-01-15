from collections import defaultdict
import bisect


class Solution:
    def findItinerary(self, tickets):
        airports, target = defaultdict(list), len(tickets) + 1
        for travel in tickets:
            a, b = travel[0], travel[1]
            bisect.insort(airports[a], b)

        def solve(src, route):
            route.append(src)
            if len(route) == target:
                return route

            for i in range(len(airports[src])):
                val = airports[src][i]
                if val != '#':
                    airports[src][i] = '#'
                    travell = solve(val, route)
                    if travell:
                        return travell
                    else:
                        airports[src][i] = val
            route.pop()
            return []

        return solve('JFK', [])


print(Solution().findItinerary(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))