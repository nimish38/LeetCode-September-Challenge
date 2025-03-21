class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if not st:
                st.append([c, 1])
            else:
                val, cnt = st[-1]
                if val == c:
                    if cnt == k - 1:
                        st.pop()
                    else:
                        st[-1][1] += 1
                else:
                    st.append([c, 1])
        res = ''
        for c, v in st:
            res += (c * v)
        return res


print(Solution().removeDuplicates(s = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", k = 4))

