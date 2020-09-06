# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: int, root2: int) -> List[int]:
    
        # inorder traversal of BTree, which returns sorted list
        def inorder(root, lst):
            if not root: return
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)
            
        r1, r2 = [], []
        inorder(root1, r1)
        inorder(root2, r2)
        i = 0
        j = 0
        res = []
        n1 = len(r1)
        n2 = len(r2)
        
        # merge sort of two sorted lists
        while(i < n1 and j < n2):
            if r1[i] < r2[j]:
                res.append(r1[i])
                i += 1
            else:
                res.append(r2[j])
                j += 1 
        
        #final answer
        #print(res + r1[i:] + r2[j:])
        return res + r1[i:] + r2[j:]
