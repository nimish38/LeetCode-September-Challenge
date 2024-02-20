class Solution:
    def uniqueOccurrences(self, arr):
        occur = dict()
        for val in arr:
            if val in occur:
                occur[val] += 1
            else:
                occur[val] = 1

        unique = occur.values()
        if len(unique) == len(set(unique)):
            return True
        return False

print(Solution().uniqueOccurrences([-17,19,-17,-17,19,2,19,-17,19,19,2,19,0,19,19]))