class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        total_ones = sum(flowerbed)
        length = len(flowerbed)
        if length%2:
            return True if length//2 + 1 >= total_ones + n else False
        else:
            return True if length//2 >= total_ones + n else False

a= Solution()
print(a.canPlaceFlowers([1,0,0,0,0,1], 2))
