import operator
class Solution:
    def evalRPN(self, tokens) -> int:
        # print(12 // -5)
        st, operators = [], {'+': operator.add, '-': operator.sub, '/': operator.floordiv, '*': operator.mul}
        for tok in tokens:
            if tok not in operators:
                st.append(int(tok))
            else:
                op2, op1 = st.pop(), st.pop()
                mul = 1
                if tok == '/' and ((op1 < 0 and op2 > 0) or (op2 < 0 and op1 > 0)):
                    mul, op1, op2 = -1, abs(op1), abs(op2)
                st.append(mul * operators[tok](op1, op2))
        return st[0]

print(Solution().evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))