import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        for i in range(len(capital)):
            if capital[i] == 0:
                w += profits[i]

        heap = []
        heapq._heapify_max(heap)

        for i in range(len(capital)):
            if capital[i] != 0:
                heapq._heapify_max(heap, (profits[i], capital[i]))

        

