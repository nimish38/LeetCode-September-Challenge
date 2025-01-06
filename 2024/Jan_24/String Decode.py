class Solution:
    def decodeString(self, s: str) -> str:
        res, stack = '', []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                curr = ''
                while stack[-1] != '[':
                    curr = stack.pop() + curr
                # pop opening bracket
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(curr * int(num))

        return ''.join(stack)

print(Solution().decodeString('2[abc]3[cd]ef'))