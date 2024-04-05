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
        print(buttons)

Solution().letterCombinations(digits = "23")