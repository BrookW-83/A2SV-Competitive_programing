class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        pointer = 0
        for i in range(1, len(prices)):
            if prices[pointer] < prices[i]:
                maxProfit = max(maxProfit, prices[i] - prices[pointer])
            else:
                pointer = i

        return maxProfit
