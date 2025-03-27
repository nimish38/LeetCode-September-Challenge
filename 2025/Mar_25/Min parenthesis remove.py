class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st, cnt = [], 0

        for c in s:
            if c == '(':
                st.append('(')
                cnt += 1
            elif c == ')':
                if cnt > 0:
                    combine = c
                    while st[-1] != '(':
                        combine = st.pop() + combine
                    st[-1] += combine
                    cnt -= 1
            else:
                if not st or st[-1] == '(':
                    st.append(c)
                else:
                    st[-1] += c



