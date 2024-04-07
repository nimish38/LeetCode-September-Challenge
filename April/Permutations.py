class Solution:
    def permute(self, nums):
        def explore(combo, options):
            if len(options) == 0:
                res.append(combo)
                return
            for item in options:
                combo.append(item)
                options.remove(item)
                explore(list(combo), set(options))
                combo.pop()
                options.add(item)
        res = []
        explore([], set(nums))
        return res

print(Solution().permute(nums = [1]))
