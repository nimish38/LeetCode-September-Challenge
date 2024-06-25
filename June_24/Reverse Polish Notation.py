import operator
class Solution:
    def evalRPN(self, tokens) -> int:
        st, operators = [], {'+': operator.add, '-': operator.sub, '/': operator.floordiv, '*': operator.mul}
        for tok in tokens:
            if tok not in operators:
                st.append(int(tok))
            else:
                op2, op1 = st.pop(), st.pop()
                st.append(operators[tok](op1, op2))
        return st[0]

print(Solution().evalRPN(tokens = ["4","13","5","/","+"]))