from collections import defaultdict
import string
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        buttons, letters, cnt = defaultdict(), string.ascii_lowercase, 0
        for i in range(2, 10):
            buttons[i] = list(letters[cnt: cnt + 3])
            cnt += 3

            if i == 7 or i == 9:
                buttons[i].append(letters[cnt])
                cnt += 1

        letters = []
        letters.extend(buttons[int(digits[0])])
        for i in range(1, len(digits)):
            for j in range(len(letters)):
                for char in buttons[int(digits[i])]:
                    letters.append(letters[j] + char)
            letters = letters[j + 1:]
        return letters

print(Solution().letterCombinations(digits = "2345"))