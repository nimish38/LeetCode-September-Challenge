from collections import deque
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

        que = deque()
        for char in buttons[digits[0]]:
            que.append(char)

        for i in range(1, len(digits)):
            curr = buttons[digits[i]]
            lvl = len(que)
            for j in range(lvl):
                word = que.popleft()
                for char in curr:
                    que.append(word + char)
        return list(que)

print(Solution().letterCombinations(digits = "234"))
