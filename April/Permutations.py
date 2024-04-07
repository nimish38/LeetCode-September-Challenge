class Solution:
    def permute(self, nums):
        def explore(combo, options):
            if len(options) == 0:
                res.append(combo)
                return
            for item in options:
                combo.append(item)
                options.remove(item)
                explore(combo, options)
                combo.pop()
                options.append(item)
        res = []
        explore([], nums)
        return res

print(Solution().permute(nums = [1,2,3]))
