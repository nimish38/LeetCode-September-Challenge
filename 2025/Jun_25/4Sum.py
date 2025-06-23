class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res, n = [], len(nums)

        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]: continue
            for b in range(a + 1, n):
                if b > a + 1 and nums[b] == nums[b - 1]: continue
                c, d = b + 1, n - 1
                while c < d:
                    val = nums[a] + nums[b] + nums[c] + nums[d]
                    if val == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    elif val < target:
                        c += 1
                    else:
                        d -= 1
        return res

print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))