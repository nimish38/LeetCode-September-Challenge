from collections import defaultdict
import string
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
        letters = []
        letters.extend(buttons[digits[0]])
        for i in range(1, len(digits)):
            for j in range(len(letters)):
                for char in buttons[digits[i]]:
                    letters.append(letters[j] + char)
            letters = letters[j + 1:]
        return letters

print(Solution().letterCombinations(digits = "2345"))