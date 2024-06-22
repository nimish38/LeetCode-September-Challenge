class Solution:
    def isValid(self, s: str) -> bool:
        match = {']': '[', '}': '{', ')': '('}
        if s[0] in match:
            return False
        st = [s[0]]
        for i in range(1, len(s)):
            if s[i] in match:
                if not st or st[-1] != match[s[i]]:
                    return False
                st.pop()
            else:
                st.append(s[i])
        return len(st) == 0

print(Solution().isValid(s = "()[]{}}"))