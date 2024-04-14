class Solution:
    def maxProfit(self, prices, fee):
        def market(ind, need_buying):
            if ind == len(prices):
                return 0

            profit = 0
            # If it is buying
            if need_buying:
                sale = market(ind + 1, False) - prices[ind]
                hold = market(ind + 1, True)
                profit = max(profit, sale, hold)
            # if it is selling
            else:
                sale = market(ind + 1, True) + prices[ind] - fee
                hold = market(ind + 1, False)
                profit = max(profit, sale, hold)
            return profit

        return market(0, True)

print(Solution().maxProfit(prices = [1,3,7,5,10,3], fee = 3))