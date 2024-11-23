class Solution:
    def numFactoredBinaryTrees(self, arr) -> int:
        fact, n = {}, len(arr)
        for val in arr:
            fact[val] = 1

        def solve(ind):
            for i in range(n):
                if i == ind:
                    continue
                if arr[ind] % arr[i] == 0:
                    x = arr[ind] // arr[i]
                    if x in fact:
                        fact[arr[ind]] += 1 + (fact[arr[i]] - 1) + (fact[x] - 1)

        for i in range(len(arr)):
            solve(i)
        return sum(fact.values())


print(Solution().numFactoredBinaryTrees(arr = [2,4,8]))
