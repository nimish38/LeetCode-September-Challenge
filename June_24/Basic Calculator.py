import operator
class Solution:
    def calculate(self, s: str) -> int:
        st, operators, neg = [], {'+': operator.add, '-': operator.sub}, False
        for char in s:
            if char == ' ':
                continue
            elif char in operators:
                if not st or st[-1] in operators:
                    neg = True
                else:
                    st.append(char)
            elif char == ')':
                num = st.pop()
                st.pop()
                st.append(num)
            elif char == '(':
                st.append(char)
            else:
                if not st:
                    st.append(int(char))
                elif neg:
                    st.append(-1 * int(char))
                elif st[-1] in operators:
                    op, num = st.pop(), st.pop()
                    st.append(operators[op](num, int(char)))
                else:
                    st.append(int(char))

        while len(st) > 1:
            op2, op, op1 = st.pop(), st.pop(), st.pop()
            st.append(operators[op](op1, op2))

        return st[0]

print(Solution().calculate(s = "(1+(4+5+2)-3)+(6+8)"))

