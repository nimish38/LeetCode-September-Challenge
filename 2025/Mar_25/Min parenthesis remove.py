class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # remove extra right parenthese )
        def remove_extra_rp(s: str) -> tuple:

            extra_lp = 0
            for l in s:
                if l == "(": extra_lp += 1
                if l == ")":
                    if extra_lp == 0:
                        s = s.replace(l, "", 1)
                    else:
                        extra_lp -= 1
            return s, extra_lp

        s, extra_lp = remove_extra_rp(s)
        s = s[::-1].replace("(", "", extra_lp)[::-1]
        return s


print(Solution().minRemoveToMakeValid(s = "))(("))

