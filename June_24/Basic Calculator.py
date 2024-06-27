import operator
class Solution:
    def calculate(self, s: str) -> int:
        st, operators, neg, start = [], {'+': operator.add, '-': operator.sub}, False, 1
        i = 0
        while i < len(s):
            char = s[i]
            if char == ' ':
                continue
            elif char in operators:
                if not st or st[-1] in operators or st[-1] == '(':
                    neg = True
                else:
                    st.append(char)
            elif char == ')':
                emt = []
                while st[-1] != '(' and st[-1] != '-(':
                    emt.append(st.pop())
                while len(emt) > 1:
                    op2, op, op1 = emt.pop(), emt.pop(), emt.pop()
                    emt.append(operators[op](op1, op2))
                minus = st.pop()
                if minus == '-(':
                    st.append(-1 * emt[0])
                else:
                    st.append(emt[0])
            elif char == '(':
                if neg:
                    st.append('-(')
                    neg = False
                else:
                    st.append(char)
            else:
                number = char
                while i + 1 < len(s) and s[i + 1].isnumeric():
                    i += 1
                    number += s[i]
                if neg:
                    st.append(-1 * int(number))
                    neg = False
                elif not st:
                    st.append(int(number))
                elif st[-1] in operators:
                    op, num = st.pop(), st.pop()
                    st.append(operators[op](num, int(number)))
                else:
                    st.append(int(number))
            i += 1

        while len(st) > 1:
            op2, op, op1 = st.pop(), st.pop(), st.pop()
            st.append(operators[op](op1, op2))

        return st[0]

print(Solution().calculate(s = "12311"))

