class Solution:
    def canVisitAllRooms(self, rooms):
        visited, stack = [0], [0]
        while len(visited) < len(rooms) - 1 and stack:
            item = stack.pop()
            for ele in rooms[item]:
                if ele not in visited:
                    visited.append(ele)
                    stack.append(ele)

        return len(visited) == len(rooms) - 1


print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))

