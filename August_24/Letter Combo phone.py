class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        buttons = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def solve(ind, curr):
            if ind >= len(digits):
                res.append(curr)
                return
            word = buttons[digits[ind]]
            for char in word:
                solve(ind + 1, curr + char)

        solve(0, "")
        return res

print(Solution().letterCombinations(digits = "234"))
