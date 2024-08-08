class Solution:
    def kthSmallest(self, root, k: int) -> int:
        curr, st = root, []
        while curr:
            st.append(curr)
            curr = curr.left

        while st or curr:
            if not curr:
                curr = st.pop()
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                while curr:
                    st.append(curr)
                    curr = curr.left

