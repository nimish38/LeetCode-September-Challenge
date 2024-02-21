from collections import Counter
class Solution:
    def closeStrings(self, word1, word2):
        cnt1, cnt2 = Counter(word1), Counter(word2)
        if cnt1.keys() == cnt2.keys():
            cnt1 = list(cnt1.values())
            cnt2 = list(cnt2.values())
            if len(cnt1) == len(cnt2):
                cnt1.sort()
                cnt2.sort()
                return cnt1 == cnt2
        return False

print(Solution().closeStrings('sabbba', 'abbccc'))