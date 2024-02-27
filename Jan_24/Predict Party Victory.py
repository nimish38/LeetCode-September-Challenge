class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate, i = list(senate), 0
        while len(set(senate)) == 2:
            if senate[i] == 'R':
                senate.remove('D')
            else:
                senate.remove('R')
            i = (i + 1) % len(senate)

        if set(senate).pop() == 'R':
            return 'Radiant'
        return 'Dire'

print(Solution().predictPartyVictory('RDD'))