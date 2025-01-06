class Solution:
    def maxProfit(self, prices, fee):
        memo = []
        for _ in range(len(prices)):
            memo.append([-1, -1])
        

        def market(ind, need_buying):
            if ind == len(prices):
                return 0
            if memo[ind][need_buying] != -1:
                return memo[ind][need_buying]

            profit = 0
            # If it is buying
            if need_buying:
                sale = market(ind + 1, 0) - prices[ind]
                hold = market(ind + 1, 1)
                profit = max(profit, sale, hold)
            # if it is selling
            else:
                sale = market(ind + 1, 1) + prices[ind] - fee
                hold = market(ind + 1, 0)
                profit = max(profit, sale, hold)

            memo[ind][need_buying] = profit
            return profit

        return market(0, 1)

print(Solution().maxProfit(prices = [1,3,2,8,4,9], fee = 2))