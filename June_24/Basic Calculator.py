class Solution:
    def calculate(self, s: str) -> int:
        num, res, sign, st = 0, 0, 1, []
        for i in range(len(s)):
            char = s[i]
            if char == ' ':
                continue
            if char.isnumeric():
                num = num*10 + int(char)

            if char == '+' or char == '-':
                res = res + (num * sign)
                num = 0
                if char == '-':
                    sign = -1
                else:
                    sign = 1

            if char == '(':
                st.append(res)
                st.append(sign)
                res, num, sign = 0, 0, 1

            if char == ')':
                res = res + (num * sign)
                num, sign = 0, 1
                res = (st.pop() * res) + st.pop()
        res = res + (num * sign)
        return res
print(Solution().calculate(s = "(1+(4+5+2)-3)+(6+8)"))

