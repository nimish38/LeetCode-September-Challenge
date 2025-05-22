class Solution(object):
    def isAlienSorted(self, words, order):
        order = {order[i] : i for i in range(26)}

        def ordered(i):
            x, y, j = words[i], words[i + 1], 0
            leng = min(len(x), len(y))
            while j < leng and x[j] == y[j]:
                j += 1
            if j == leng and j == len(y):
                return True
            if j == leng and j == len(x):
                return False
            return order[x[j]] < order[y[j]]

        for i in range(len(words) - 1):
            if not ordered(i):
                return False
        return True


print(Solution().isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))