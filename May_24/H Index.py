class Solution:
    def hIndex(self, citations):
        citations.sort()
        i, n = len(citations) - 1, len(citations)
        while i >= 0 and citations[i] >= n - i:
                i -= 1
        return n - i - 1

print(Solution().hIndex(citations = [3,0,6,1,5]))