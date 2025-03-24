class Solution:
    def permute(self, nums):
        res, n = [], len(nums)

        def solve(arr, combo):
            if len(combo) == n:
                res.append(list(combo))
                return
            for i in range(len(arr)):
                x = arr.pop(i)
                combo.append(x)
                solve(arr, combo)
                arr.insert(i, x)
                combo.pop()

        solve(nums, [])
        return res


print(Solution().permute(nums = [1,2,3]))