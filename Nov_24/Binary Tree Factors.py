class Solution:
    def numFactoredBinaryTrees(self, arr) -> int:
        fact = [1]*(len(arr))

        def solve(ind):
            for i in range(ind):
                for j in range(ind):
                    if arr[i] * arr[j] == arr[ind]:
                        fact[ind] += 1

        for i in range(1, len(arr)):
            solve(i)
        return sum(fact)


print(Solution().numFactoredBinaryTrees(arr = [2,4,5,10]))
