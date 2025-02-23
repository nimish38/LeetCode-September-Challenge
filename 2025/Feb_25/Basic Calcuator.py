class Solution:
    def calculate(self, s: str) -> int:
        st, i, neg = [], 0, 1
        while i < len(s):
            if s[i].isnumeric():
                num = ''
                while s[i].isnumeric():
                    num += s[i]
                    i += 1
                st.append(int(num) * neg)
                neg = 1
            if s[i] == ')':
                while st[-1] != '(' and st[-2] in ['-', '+']:
                    op2, opr, op1 = st.pop(), st.pop(), st.pop()
                    if opr == '-':
                        val = op1 - op2
                    else:
                        val = op1 + op2
                    st.append(val)
                num = st.pop()
                st.pop()
                st.append(num * neg)
                neg = 1
            elif s[i] == '-' and not st or st[-1] == '(':
                neg = -1
            else:
                st.append(s[i])
            i += 1
        while len(st) > 1:
            op2, opr, op1 = st.pop(), st.pop(), st.pop()
            if opr == '-':
                val = int(op1) - int(op2)
            else:
                val = int(op1) + int(op2)
            st.append(val)
        return st[0]


print(Solution().calculate(s = "-1-(4+5+2)"))