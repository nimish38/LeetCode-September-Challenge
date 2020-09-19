class Solution:
    def maxProfit(self, nums):
        # set max and min
        mx = 0
        mn = 10000000000000
        
        for i in nums:
            # if current price is less than min update min
            if i < mn:
                mn = i
            # store maximum profit upto current day    
            else:
                mx = max(mx,i - mn)
        
        return mx