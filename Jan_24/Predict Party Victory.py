from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate= list(senate)
        dire, rad = deque(), deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                rad.append(i)
            else:
                dire.append(i)

        while rad and dire:
            radIndx, dirIndx = rad.popleft(), dire.popleft()
            if radIndx < dirIndx:
                rad.append(radIndx+len(senate))
            else:
                dire.append(dirIndx+len(senate))

        return "Radiant" if rad else "Dire"

print(Solution().predictPartyVictory('RDD'))