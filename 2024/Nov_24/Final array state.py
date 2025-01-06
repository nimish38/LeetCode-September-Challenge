import heapq


class Solution:
    def getFinalState(self, nums, k: int, multiplier: int):
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))
        heapq.heapify(arr)
        for _ in range(k):
            val, ind = heapq.heappop(arr)
            heapq.heappush(arr, (val * multiplier, ind))

        for _ in range(len(nums)):
            nums[arr[_][1]] = arr[_][0]
        return nums

print(Solution().getFinalState(nums = [2,1,3,5,6], k = 5, multiplier = 2))
