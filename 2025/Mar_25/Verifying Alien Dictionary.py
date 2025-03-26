class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        pos = {}

        def lexo(first, second):
            run = min(len(first), len(second))
            for i in range(run):
                if pos[first[i]] < pos[second[i]]:
                    return True
                elif pos[first[i]] > pos[second[i]]:
                    return False
            if len(second) > run:
                return False
            return True

        for i in range(len(order)):
            pos[order[i]] = i

        for i in range(len(words)):
            if not lexo(words[i - 1], words[i]):
                return False
        return True
