class Solution(object):
    def minEnd(self, n, x):
        res, x_ptr, n_ptr, target = x, 1, 1, n - 1
        while n_ptr <= target:
            if x_ptr & x == 0:
                if n_ptr & target != 0:
                    res = res | x_ptr
                n_ptr <<= 1
            x_ptr <<= 1
        return res

print(Solution().minEnd(n = 5, x = 4))