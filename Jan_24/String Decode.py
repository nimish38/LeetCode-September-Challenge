class Solution:
    def decodeString(self, s: str) -> str:
        res, stack = '', []
        for char in s:
            if char is ']':
                curr = ''
                while stack[-1] != '[':
                    curr = stack.pop() + curr
                # pop opening bracket
                stack.pop()
                num = ''
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                num = int(num)
                stack.append(curr * num)
            else:
                stack.append(char)

        while stack:
            res = stack.pop() + res
        return res

print(Solution().decodeString('2[abc]3[cd]ef'))