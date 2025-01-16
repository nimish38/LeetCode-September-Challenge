from collections import defaultdict
import bisect


class Solution:
    def findItinerary(self, tickets):
        airports, target, res, st = defaultdict(list), len(tickets) + 1, [], ['JFK']
        for travel in tickets:
            a, b = travel[0], travel[1]
            airports[a].append(b)
        for city in airports:
            airports[city].sort(reverse=True)

        # def solve(src, route):
        #     route.append(src)
        #     if len(route) == target:
        #         self.res = route
        #         return True
        #
        #     for i in range(len(airports[src])):
        #         val = airports[src][-1]
        #         airports[src].pop()
        #         if solve(val, route):
        #             return True
        #         airports[src].append(val)
        #     route.pop()
        #     return False

        while st:
            city = st[-1]
            if city in airports and airports[city]:
                st.append(airports[city].pop())
            else:
                # this gets all cities that have 0 in degree one by one
                res.append(st.pop())
        return res[::-1]



print(Solution().findItinerary(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))