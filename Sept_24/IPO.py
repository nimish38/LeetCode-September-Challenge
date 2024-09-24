import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        pairs = []
        for i in range(len(capital)):
            if capital[i] == 0:
                pairs.append((capital[i], profits[i]))
        pairs.sort()
    


print(Solution().findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))

