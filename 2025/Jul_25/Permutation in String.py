from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        s1, cnt = Counter(s1), len(s1)

        def check(i):
            dic = s1.copy()
            for ind in range(i, i + cnt):
                if s2[ind] not in dic:
                    return False
                dic[s2[ind]] -= 1
                if dic[s2[ind]] == 0:
                    del dic[s2[ind]]
            return True

        for i in range(len(s2) - cnt + 1):
            if s2[i] in s1 and check(i):
                return True
        return False

print(Solution().checkInclusion(s1 = "adc", s2 = "dcda"))