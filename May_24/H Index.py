class Solution:
    def hIndex(self, citations):
        citations.sort()
        i, n = 0, len(citations)
        while citations[i] < n - i:
            i += 1
        return n - i

print(Solution().hIndex(citations = [0, 1, 3, 6]))