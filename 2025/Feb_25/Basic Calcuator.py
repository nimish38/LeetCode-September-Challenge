class Solution:
    def calculate(self, s: str) -> int:
        current, result, sign, st = 0, 0, 1, []
        for c in s:
            if c.isnumeric():
                current = (current * 10) + int(c)
            elif c == '+' or c == '-':
                result += current * sign
                if c == '-':
                    sign = -1
                else:
                    sign = 1
            elif c == '(':
                st.append(result)
                st.append(sign)
                current, result, sign = 0, 0, 1
            else:
                result += current * sign
                operand, prev_res = st.pop(), st.pop()
                result, current, sign = result * operand + prev_res, 0, 1
        result += current * sign
        return result


print(Solution().calculate(s = "1-(-2)"))