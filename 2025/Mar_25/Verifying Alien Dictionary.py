class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        pos = {}
        for i in range(len(order)):
            pos[order[i]] = i

        for i in range(len(words)):
            if not lexo(words[i - 1], words[i]):
                return False
        return True
