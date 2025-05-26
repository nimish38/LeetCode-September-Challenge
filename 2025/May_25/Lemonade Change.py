from collections import defaultdict


class Solution(object):
    def lemonadeChange(self, bills):
        purse, cnt = 0, defaultdict(int)
        for bill in bills:
            if bill == 5:
                purse += bill
                cnt[5] += 1
            elif bill == 10:
                if purse == 0 or cnt[5] == 0:
                    return False
                purse += 5
                cnt[5] -= 1
                cnt[10] += 1
            else:
                if purse < 15 or (cnt[10] == 0 and cnt[5] < 3) or cnt[5] == 0:
                    return False
                if cnt[10] > 0:
                    cnt[10] -= 1
                    cnt[5] -= 1
                else:
                    cnt[5] -= 3
                purse += 5
                cnt[20] += 1
        return True