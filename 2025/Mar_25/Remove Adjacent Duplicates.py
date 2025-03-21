class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if len(st) >= k - 1:
                curr = set(st[len(st) - k + 1:])
                curr.add(c)
                if len(curr) == 1:
                    del st[len(st) - k + 1:]
                else:
                    st.append(c)
            else:
                st.append(c)
        return ''.join(st)


print(Solution().removeDuplicates(s = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", k = 4))

