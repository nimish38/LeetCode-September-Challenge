
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
                node = st.pop()
                value = node.val
                if value not in hashmap:
                    hashmap[value] = Node(value)
                    for elem in node.neighbors:
                        if elem.val in hashmap:
                            hashmap[value].neighbprs.append(hashmap[elem.val])
                        else:
                            st.append(elem)

        dfs(node)
        return hashmap[1]