
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        hashmap = {}

        def dfs(val):
            st = [val]
            while st:
                vertex = st.pop()
                if vertex not in hashmap:
                    hashmap[vertex] = Node(vertex)
                    for elem in vertex.neighbors:
                        if elem not in hashmap:
                            st.append(elem)
        dfs(node)

        for elem in hashmap:
            target = hashmap[elem]
            for nei in elem.neighbors:
                target.neighbors.append(hashmap[nei])

        return hashmap[node]