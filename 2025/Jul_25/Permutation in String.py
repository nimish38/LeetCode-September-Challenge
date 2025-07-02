class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False
        main, side, j, i = {}, {}, len(s1), 0
        for _ in range(97, 123):
            main[chr(_)] = 0
            side[chr(_)] = 0

        for _ in range(len(s1)):
            main[s1[_]] += 1
            side[s2[_]] += 1

        while j < len(s2):
            if main == side:
                return True
            side[s2[j]] += 1
            j += 1
            side[s2[i]] -= 1
            i += 1
        return main == side

print(Solution().checkInclusion(s1 = "adc", s2 = "dcda"))