class Solution:
    def maxSatisfied(self, customers, grumpy, minutes: int) -> int:
        gr_tot, ngr_tot, i, j = 0, 0, 0, 0
        for k in range(len(customers)):
            if j < minutes and grumpy[k]:
                gr_tot += customers[k]
                j += 1
            if not grumpy[k]:
                ngr_tot += customers[k]

        