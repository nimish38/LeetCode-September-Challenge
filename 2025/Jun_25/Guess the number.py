def guess(num):
    return num // 2

class Solution(object):
    def guessNumber(self, n):
        l, r = 1, n
        while l <= r:
            mid = l + ((r - l) // 2)
            ans = guess(mid)
            if ans == 0:
                return mid
            if ans == -1:
                r = mid - 1
            else:
                l = mid + 1
        return -1
