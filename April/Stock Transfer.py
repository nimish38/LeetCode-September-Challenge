class Solution:
    def maxProfit(self, prices, fee):
        def market(purchase, curr_profit, ind):
            if ind == len(prices):
                return curr_profit

            # Transaction
            if purchase == -1:
                return max(market(prices[ind], curr_profit, ind + 1), market(purchase, curr_profit, ind + 1))
            sale = 0
            if prices[ind] - fee - purchase > 0:
                sale = market(-1, curr_profit + prices[ind] - fee - purchase, ind + 1)
            return max(sale, market(purchase, curr_profit, ind + 1))

        return market(-1, 0, 0)

print(Solution().maxProfit(prices = [1,3,7,5,10,3], fee = 3))