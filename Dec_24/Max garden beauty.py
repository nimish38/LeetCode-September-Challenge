class Solution:
    def maximumBeauty(self, flowers: list, newFlowers: int, target: int, full: int, partial: int) -> int:
        n, curr = len(flowers), 0
        flowers.sort(reverse=True)

        addition = [0] * n
        for i in range(n - 2, -1, -1):
            addition[i] = ((flowers[i] - flowers[i + 1]) * (n - 1 - i)) + addition[i + 1]

        while curr < n and flowers[curr] >= target:
            curr += 1


