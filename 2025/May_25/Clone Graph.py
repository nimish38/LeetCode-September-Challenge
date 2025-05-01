
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        vis, st, clone = set(), [node], {}
        while st:
            value = st.pop()
            if value.val not in vis:
                vis.add(value.val)
                clone[value] = Node(value.val)
                for nei in value.neighbors:
                    if nei not in vis:
                        st.append(nei)

        for item in clone:
            new_nei = []
            for nei in item.neighbors:
                new_nei.append(clone[nei])
            clone[item].neighbors = new_nei
        return clone[node]
