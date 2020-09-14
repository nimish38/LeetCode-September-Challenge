class Solution:
    def rob(self, nums: List[int]) -> int:
        # max sum including current num, excluding current num
        incl, excl = 0, 0       
        
        for curr in nums:
            # store old inclusive sum
            old_incl = incl
            # get max of last inclusive sum or addition of current number and exclusing previous num
            incl = max(incl, excl + curr)
            # store old inclusive sum
            excl = old_incl
        return max(incl, excl)    