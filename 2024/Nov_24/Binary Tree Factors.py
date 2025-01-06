class Solution:
    def numFactoredBinaryTrees(self, arr) -> int:
        fact, n = {}, len(arr)
        arr.sort()
        for val in arr:
            fact[val] = 1

        def solve(ind):
            for i in range(ind):
                if arr[ind] % arr[i] == 0:
                    x = arr[ind] // arr[i]
                    if x in fact:
                        fact[arr[ind]] += fact[arr[i]] * fact[x]

        for i in range(len(arr)):
            solve(i)
        return sum(fact.values()) % ((10**9) + 7)


print(Solution().numFactoredBinaryTrees(arr = [2,4,8]))
