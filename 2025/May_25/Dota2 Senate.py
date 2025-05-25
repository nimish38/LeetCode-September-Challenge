class Solution(object):
    def predictPartyVictory(self, senate):
        rad, dire, cnt, n = 0, 0, 0, len(senate)
        for c in senate:
            if c == 'R':
                rad += 1
            else:
                dire += 1
        senate, ind = list(senate), 0
        while rad > 0 and dire > 0:
            c = senate[ind]
            if c == 'R':
                if cnt < 0:
                    senate[ind] = 'X'
                    rad -= 1
                cnt += 1
            elif c == 'D':
                if cnt > 0:
                    senate[ind] = 'X'
                    dire -= 1
                cnt -= 1
            ind = (ind + 1) % n
        return 'Radiant' if dire == 0 else 'Dire'

print(Solution().predictPartyVictory('RDRDDRD'))