class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        holding = -prices[0]
        idle = 0
        sold = 0

        for i in range(1, n):
            prev_holding = holding
            prev_idle = idle
            prev_sold = sold
            holding = max(holding, prev_idle - prices[i])
            sold = prev_holding + prices[i]
            idle = max(idle, prev_sold)

       
 
        return max(sold, idle)
        
