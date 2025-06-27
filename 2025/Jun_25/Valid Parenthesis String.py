class Solution(object):
    def checkValidString(self, s):
        st, opencnt, starcnt = [], 0, 0
        for c in s:
            if c == ')':
                if not st:
                    return False
                if st[-1] == '(':
                    st.pop()
                else:
                    if len(st) >= 2 and st[-2] == '(':
                        val = st.pop()
                        st.pop()
                        if st:
                            if st[-1] == '(':
                                st.append(val)
                            else:
                                st[-1] += val
                        else:
                            st.append(val)
                    else:
                        val = st.pop() - 1
                        if val > 0:
                            if st:
                                if st[-1] == '(':
                                    st.append(val)
                                else:
                                    st[-1] += val
                            else:
                                st.append(val)
            elif c == '*':
                if not st or st[-1] == '(':
                    st.append(1)
                else:
                    st.append(st.pop() + 1)
            else:
                st.append(c)

        for _ in st:
            if _ == '(':
                opencnt += 1
            else:
                starcnt += _

        if opencnt == 0 or opencnt == starcnt:
            return True
        return False

print(Solution().checkValidString(s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))