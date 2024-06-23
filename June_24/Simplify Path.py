class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        for dir in path.split('/'):
            if dir == '' or dir == '.':
                continue
            if dir == '..':
                if st:
                    st.pop()
            else:
                st.append(dir)

        return '/' + '/'.join(st)

print(Solution().simplifyPath("/.../a/../b/c/../d/./"))