class Solution:
    def removeCyclic(self, arr, delete, i):
        for _ in range(len(arr) + 1):
            if arr[i] == delete:
                del arr[i]
                return
            i = (i+1) % len(arr)

    def predictPartyVictory(self, senate: str) -> str:
        senate, i = list(senate), 0
        while len(set(senate)) == 2:
            if senate[i] == 'R':
                self.removeCyclic(senate,'D', i)
            else:
                self.removeCyclic(senate, 'R', i)
            if i + 1 >= len(senate):
                i = 0
            else:
                i += 1

        if set(senate).pop() == 'R':
            return 'Radiant'
        return 'Dire'

print(Solution().predictPartyVictory('DRRD'))