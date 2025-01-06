class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root):
        queue, maxSum, curSum, MaxLvl, curLvl = [root], float("-inf"), float("-inf"), -1, 0
        while queue:
            curLvl += 1
            curSum = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                curSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if curSum > maxSum:
                maxSum = curSum
                maxLvl = curLvl
        return maxLvl

a = TreeNode(989)
a.right = TreeNode(10250)
a.right.left = TreeNode(98693)
a.right.right = TreeNode(-89388)
a.right.right.right = TreeNode(-32127)
print(Solution().maxLevelSum(a))