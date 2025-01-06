class Solution:
    def permute(self, nums):
        def explore(combo):
            if len(combo) == len(nums):
                res.append(combo)
                return
            for item in nums:
                if item not in combo:
                    combo.append(item)
                    explore(list(combo))
                    combo.pop()
        res = []
        explore([])
        return res

print(Solution().permute(nums = [1, 2, 3]))
