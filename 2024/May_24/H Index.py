class Solution:
    def hIndex(self, citations):
        citations.sort()
        n, cnt = len(citations), 0
        for i in range(n-1, -1, -1):
            if citations[i] >= n-i:
                cnt = n - i
            else:
                break
        return cnt

print(Solution().hIndex(citations = [3,0,6,1,5]))