from collections import defaultdict
import bisect


class Solution:
    def findItinerary(self, tickets):
        airports, cnt = defaultdict(list), len(tickets)
        for travel in tickets:
            a, b = travel[0], travel[1]
            bisect.insort(airports[a], b)
        target = cnt + 1 - (cnt // 2)

        def solve(src, route):
            if len(route) == target - 1:
                return route.append(src)

            for i in range(airports[src]):
                val = airports[src][i]
                if val != '#':
                    airports[src][i] = '#'
                    travel = solve(val, route.append(src))
                    if travel:
                        return travel
                    else:
                        airports[src][i] = val
            return []


        return solve('JFK', [])


print(Solution().findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))