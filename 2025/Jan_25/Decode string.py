class Solution:
    def decodeString(self, s: str) -> str:
        st, res, i = [], '', 0
        while i < len(s):
            if s[i] == ']':
                curr, num = '', ''
                while st[-1] != '[':
                    curr = st.pop() + curr
                st.pop()
                while st and st[-1].isnumeric():
                    num = st.pop() + num
                st.append(curr * int(num))
            else:
                st.append(s[i])
            i += 1
        return ''.join(st)


print(Solution().decodeString(s = "2[abc]3[cd]ef"))
