class Solution:
    def summaryRanges(self, nums):
        n = len(nums)
        if n == 0: return []
        if n == 1: return [str(nums[0])]
        ranges, left, right = [], 0, 1

        def build_range(l, r):
            if l == r - 1:
                ranges.append(str(nums[l]))
            else:
                ranges.append(str(nums[l]) + '->' + str(nums[r - 1]))

        while right < n:
            if nums[right] - nums[right - 1] == 1:
                right += 1
            else:
                build_range(left, right)
                left, right = right, right + 1
        build_range(left, right)
        return ranges

print(Solution().summaryRanges(nums = [0,2,3,4,6,8,9]))