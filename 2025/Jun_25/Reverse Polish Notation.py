import operator


class Solution(object):
    def evalRPN(self, tokens):
        st, oper = [], {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
        for tok in tokens:
            if tok in oper:
                two, one = st.pop(), st.pop()
                if tok == '/':
                    sign1, sign2 = 1, 1
                    if one < 0:
                        sign1, one = -1, -one
                    if two < 0:
                        sign2, two = -1, -two
                res = oper[tok](one, two)
                if tok == '/':
                    res = res * sign2 * sign1
                st.append(res)
            else:
                st.append(int(tok))
        return st[0]

print(Solution().evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))