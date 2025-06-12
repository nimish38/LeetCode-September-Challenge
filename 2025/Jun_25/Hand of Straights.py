from collections import Counter


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        cnt = Counter(hand)
        cnt = dict(sorted(cnt.items()))
        while cnt:
            first = next(iter(cnt))
            for i in range(groupSize):
                if first + i not in cnt:
                    return False
                cnt[first + i] -= 1
                if cnt[first + i] == 0:
                    del cnt[first + i]
        return True

print(Solution().isNStraightHand(hand = [8,8,9,7,7,7,6,7,10,6], groupSize = 2))