from collections import deque


class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        n, cumulative, res, mono, j = len(nums), [], float('inf'), deque(), 0
        while j < n:
            if j == 0:
                cumulative.append(nums[j])
            else:
                cumulative.append(cumulative[j - 1] + nums[j])
            if cumulative[j] >= k:
                res = min(res, j + 1)
            # check if value can be shrunk
            while mono and cumulative[j] - cumulative[mono[0]] >= k:
                res = min(res, j - mono[0])
                mono.popleft()
            # check increasing subsequence
            while mono and cumulative[j] < cumulative[mono[-1]]:
                mono.pop()

            mono.append(j)
            j += 1
        if res == float('inf'):
            return -1
        return res



print(Solution().shortestSubarray(nums = [2,-1,2], k = 3))
