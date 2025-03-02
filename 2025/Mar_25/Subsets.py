class Solution:
    def subsets(self, nums):
        n, res = len(nums), []

        def solve(curr, elem):
            if len(elem) == 0:
                return
            curr.append(elem.pop())
            res.append(curr)
            for i in range(len(elem)):
                res.append(curr.append(elem[i]))
                curr.pop()
            solve(curr, elem)
            
        solve([], nums)
        return res