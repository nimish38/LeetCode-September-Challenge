from collections import defaultdict
import bisect


class Solution:
    def findItinerary(self, tickets):
        airports = defaultdict(list)
        for travel in tickets:
            a, b = travel[0], travel[1]
            bisect.insort(airports[a], b)

        return solve('JFK')


print(Solution().findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))