class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        right = 1

        while right < len(prices):
            profit= 0
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            
            right += 1
        return maxProfit
