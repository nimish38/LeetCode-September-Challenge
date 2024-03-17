class Solution:
    def canVisitAllRooms(self, rooms):
        visited, stack = {0}, [0]
        while len(visited) < len(rooms) and stack:
            item = stack.pop()
            for ele in set(rooms[item]) - visited:
                if ele not in visited:
                    visited.add(ele)
                    stack.append(ele)

        return len(visited) == len(rooms)


print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))

