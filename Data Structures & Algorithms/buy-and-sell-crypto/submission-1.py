class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        maxProfit = 0
#prices = [10,1,5,6,7,1]
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            else:
                left = right
            
            right += 1
        return maxProfit