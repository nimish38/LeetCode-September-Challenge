class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        st, map = [node], {}
        while st:
            vertex = st.pop()
            if vertex not in map:
                clone = Node(vertex.val)
                map[vertex] = clone
                for nei in vertex.neighbors:
                    if nei not in map:
                        st.append(nei)

        for original in map:
            cloned, neighs = map[original], []
            for nei in original.neighbors:
                neighs.append(map[nei])
            cloned.neighbors = neighs

        return map[node]