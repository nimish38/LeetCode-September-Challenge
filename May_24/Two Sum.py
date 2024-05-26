class Solution:
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1
        while i < j:
            curr = numbers[i] + numbers[j]
            if curr == target:
                return [i + 1, j + 1]
            elif curr < target:
                i += 1
            else:
                j -= 1

print(Solution().twoSum(numbers = [2,7,11,15], target = 9))

