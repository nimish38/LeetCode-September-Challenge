class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        for dir in path.split('/'):
            if dir == '':
                continue
            if dir == '..':
                if st:
                    st.pop()
            else:
                st.append(dir)

        return '/' + '/'.join(st)

print(Solution().simplifyPath("/home/user/Documents/../Pictures"))