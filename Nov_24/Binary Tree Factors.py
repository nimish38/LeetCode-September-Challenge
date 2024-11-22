class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        cnt, fact = len(arr), [0]*(len(arr))
        for i in range(1, len(arr)):
            fact[i] = solve(i)

        return sum(fact) + cnt
