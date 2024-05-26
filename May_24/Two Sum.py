import bisect
class Solution:
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1
        while i < j:
            curr = numbers[i] + numbers[j]
            if curr == target:
                return [i + 1, j + 1]
            elif curr < target:
                i = bisect.bisect_left(numbers, target - numbers[j], i + 1, j)
            else:
                j = bisect.bisect_right(numbers, target - numbers[i], i + 1, j) - 1

print(Solution().twoSum(numbers = [-3,3,4,90], target = 0))

