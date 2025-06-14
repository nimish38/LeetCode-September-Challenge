class Solution(object):
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1
        while i < j:
            val = numbers[i] + numbers[j]
            if val == target:
                return [i + 1, j + 1]
            if val > target:
                j -= 1
            else:
                i += 1
        return []