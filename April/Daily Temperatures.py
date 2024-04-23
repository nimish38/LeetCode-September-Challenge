class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0]*len(temperatures)
        for i in range(len(temperatures) - 1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))