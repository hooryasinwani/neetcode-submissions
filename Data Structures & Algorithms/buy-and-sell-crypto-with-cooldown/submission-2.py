class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = -prices[0]
        idle = 0
        sold = 0

        for i in range(1, len(prices)):
            prev_holding = holding
            prev_sold = sold
            prev_idle = idle

            holding = max(prev_holding, prev_idle -prices[i])
            sold = prev_holding+prices[i]
            idle = max(idle, prev_sold)
        return max(idle, sold)
        
