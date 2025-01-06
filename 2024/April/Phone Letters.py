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

        def backtrack(idx, current_str):
            if idx == len(digits):
                res.append(current_str)
                return
            for char in buttons[digits[idx]]:
                backtrack(idx + 1, current_str + char)

        res = []
        backtrack(0, "")
        return res

print(Solution().letterCombinations(digits = "23"))