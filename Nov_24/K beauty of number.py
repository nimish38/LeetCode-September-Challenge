class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums, cnt = str(num), 0
        for i in range(0, len(nums) - k):
            val = int(nums[i: i + k])
            if val != 0 and num % val == 0:
                cnt += 1
        return cnt