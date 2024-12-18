class Solution:
    def maximumBeauty(self, flowers: list, newFlowers: int, target: int, full: int, partial: int) -> int:
        n, curr, res = len(flowers), 0, 0
        flowers.sort(reverse=True)

        addition = [0] * n
        for i in range(n - 2, -1, -1):
            addition[i] = ((flowers[i] - flowers[i + 1]) * (n - 1 - i)) + addition[i + 1]

        while curr < n and flowers[curr] >= target:
            curr += 1

        while curr < n:
            res = curr * full
            ## get max distribution as partial at this stage
            temp, x = newFlowers, curr
            while addition[x] >= temp:
                x += 1
            temp -= addition[x]
            val = addition[x]
            val += temp // (n - curr)
            parsum = partial * (n - curr)
            res = max(res,res + parsum)
            curr += 1
        return res


