class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Runtime: O(n)
        # Space: O(1)

        # Start at index 1
        # If the previous price is less than the current price,
        # we will buy at the previous price and sell at the current price
            # That is, add to current profit by curr price - prev price

        profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]
        
        return profit