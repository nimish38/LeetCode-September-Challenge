class Solution:
    def maxSatisfied(self, customers, grumpy, minutes: int) -> int:
        gr_tot, ngr_tot, i, res, j = 0, 0, 0, 0, 0
        for k in range(len(customers)):
            if j < minutes and grumpy[k]:
                gr_tot += customers[k]
            if not grumpy[k]:
                ngr_tot += customers[k]
            j += 1

        res, i, j = gr_tot + ngr_tot, 1, minutes
        while j < len(customers):
            if grumpy[i - 1]:
                gr_tot -= customers[i - 1]
            if grumpy[j]:
                gr_tot += customers[j]
            res = max(res, gr_tot + ngr_tot)
            i += 1
            j += 1
        return res


print(Solution().maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3))