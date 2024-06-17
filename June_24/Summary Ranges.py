class Solution:
    def summaryRanges(self, nums):
        n = len(nums)
        if n == 0: return []
        if n == 1: return [str(nums[0])]
        ranges, left, right = [], 0, 1
        while right < n:
            if nums[right] - nums[right - 1] == 1:
                right += 1
            else:
                if left == right - 1:
                    ranges.append(str(nums[left]))
                else:
                    ranges.append(str(nums[left]) + '->' + str(nums[right - 1]))
                left, right = right, right + 1

        if left == right - 1:
            ranges.append(str(nums[left]))
        else:
            ranges.append(str(nums[left]) + '->' + str(nums[right - 1]))

        return ranges

print(Solution().summaryRanges())