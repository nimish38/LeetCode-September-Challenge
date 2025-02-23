class Solution:
    def calculate(self, s: str) -> int:
        st = []
        for c in s:
            if c == ')':
                while st[-1] != '(':
                    op2, opr, op1 = st.pop(), st.pop(), st.pop()
                    if opr == '-':
                        val = int(op1) - int(op2)
                    else:
                        val = int(op1) + int(op2)
                    st.append(val)
                st.pop()
            else:
                st.append(c)
        while len(st) > 1:
            op2, opr, op1 = st.pop(), st.pop(), st.pop()
            if opr == '-':
                val = int(op1) - int(op2)
            else:
                val = int(op1) + int(op2)
            st.append(val)
        return st[0]


