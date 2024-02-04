class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        i = 1
        while i < len(flowerbed) - 1 and n > 0:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            i += 1

        if n:
            return False
        return True

a= Solution()
print(a.canPlaceFlowers([0, 1, 0], 1))
