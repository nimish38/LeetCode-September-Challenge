class Solution:
    # def isAlmostDistinct(self, freq: dict, m):
    #     for v in freq.values():
    #         if v > 1: return False
    #     return True

    def firstWindow(self, nums, k):
        freq = {}
        s = 0
        for i in range(k):
            s += nums[i]
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        return freq, s

    def maxSum(self, nums, m: int, k: int) -> int:
        freq, s = self.firstWindow(nums, k)
        maxs = s if len(freq) >= m else 0

        for i in range(k, len(nums)):
            added = nums[i]
            removed = nums[i - k]

            s = s + added - removed

            if freq[removed] == 1:
                del freq[removed]
            else:
                freq[removed] -= 1

            if added in freq:
                freq[added] += 1
            else:
                freq[added] = 1

            if len(freq) >= m and s > maxs: maxs = s

        return maxs

print(Solution().maxSum(nums = [5,9,9,2,4,5,4], m = 1, k = 3))