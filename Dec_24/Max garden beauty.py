class Solution:
    def maximumBeauty(self, flowers: list, newFlowers: int, target: int, full: int, partial: int) -> int:
        n, curr, res, ans = len(flowers), 0, 0, 0
        flowers.sort(reverse=True)

        addition = [0] * n
        for i in range(n - 2, -1, -1):
            addition[i] = ((flowers[i] - flowers[i + 1]) * (n - 1 - i)) + addition[i + 1]

        while curr < n and flowers[curr] >= target:
            curr += 1

        while curr < n:
            res = curr * full
            ## get max distribution as partial at this stage
            temp, x, val = newFlowers, curr, target - 1
            while x < n and addition[x] >= temp:
                x += 1
            if x < n:
                val = min(target - 1, addition[x])
            temp -= val
            val += temp // (n - curr)
            parsum = partial * (n - curr)
            ans = max(ans, res + parsum)

            newFlowers -= target - flowers[curr]
            curr += 1
        return res

print(Solution().maximumBeauty(flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1))
