class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # leetcode prompt https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

        # cache lowest price we have seen so far (running)
        # cache our running maxProfit to update and return 
        # loop through every prices and check if: 
        #   1) the curProfit is greater than maxProfit 
        #   2) if cur price is less than our cached lowest price, yes => update cached
        
        maxProfit = 0
        minPrice = prices[0]
        
        for i in range(1, len(prices)):
            maxProfit = max(prices[i] - minPrice, maxProfit)
            minPrice = min(prices[i], minPrice)
            
        return maxProfit
            