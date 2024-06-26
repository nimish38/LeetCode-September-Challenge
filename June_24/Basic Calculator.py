import operator
class Solution:
    def calculate(self, s: str) -> int:
        st, operators, neg = [], {'+': operator.add, '-': operator.sub}, False
        for char in s:
            if char == ' ':
                continue
            elif char in operators:
                if not st or st[-1] in operators or st[-1] == '(':
                    neg = True
                else:
                    st.append(char)
            elif char == ')':
                emt = []
                while st[-1] != '(':
                    emt.append(st.pop())
                while len(emt) > 1:
                    op2, op, op1 = emt.pop(), emt.pop(), emt.pop()
                    emt.append(operators[op](op1, op2))
                st.pop()
                st.append(emt[0])
            elif char == '(':
                st.append(char)
            else:
                if neg:
                    st.append(-1 * int(char))
                    neg = False
                elif not st:
                    st.append(int(char))
                elif st[-1] in operators:
                    op, num = st.pop(), st.pop()
                    st.append(operators[op](num, int(char)))
                elif type(st[-1]) is int:
                    st[-1] = (st[-1] * 10) + int(char)
                else:
                    st.append(int(char))

        while len(st) > 1:
            op2, op, op1 = st.pop(), st.pop(), st.pop()
            st.append(operators[op](op1, op2))

        return st[0]

print(Solution().calculate(s = "-2+ 1"))

