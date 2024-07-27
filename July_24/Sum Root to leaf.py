class Solution:
    def sumNumbers(self, root) -> int:
        st, nums = [(root, str(root.val))], []
        while st:
            node, curr = st.pop()
            if not node.left and not node.right:
                nums.append(int(curr))
            if node.left:
                st.append((node.left, curr + str(node.left.val)))
            if node.right:
                st.append((node.right, curr + str(node.right.val)))
        return sum(nums)

