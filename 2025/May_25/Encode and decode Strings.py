class Solution:

    def encode(self, strs) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '|' + word + '|'
        return res

    def decode(self, s: str):
        if not s:
            return []
        strs, i = [], 0
        while i < len(s):
            num = ''
            while s[i] != '|':
                num += s[i]
                i += 1
            i += 1
            num = int(num)
            strs.append(s[i : i + num])
            i += num + 1
        return strs




x = Solution().encode(["neet","code","love","you"])
print(Solution().decode(x))