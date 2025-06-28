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

        for i in range(len(st) - 1, -1, -1):
            _ = st[i]
            if _ == '(':
                starcnt -= 1
                if starcnt < 0:
                    return False
            else:
                starcnt += _
        return True


print(Solution().checkValidString(s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))