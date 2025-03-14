class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        ratio, sum, minEff = [], 0, float('-inf')
        for i in range(n):
            ratio.append((speed[i] / efficiency[i], i))
        ratio.sort(key=lambda x: x[0], reverse=True)
        for i in range(k):
            sum += sum[ratio[i][1]]
            minEff = min(minEff, efficiency[ratio[i][1]])
        return sum * minEff

    
