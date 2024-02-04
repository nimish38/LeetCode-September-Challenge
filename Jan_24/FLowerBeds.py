class Solution:
    def canPlaceFlowers(self, flowerbed, n):

        if flowerbed[0]==0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        i = 2
        while i < len(flowerbed) - 2 and n > 0:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            i += 1

        if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            n -= 1

        if n:
            return False
        return True

a= Solution()
print(a.canPlaceFlowers([0,0,1,0,1], 1))
