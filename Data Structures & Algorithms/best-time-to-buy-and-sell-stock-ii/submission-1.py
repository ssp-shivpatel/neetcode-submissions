class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy solution
            # Runtime: O(n)
            # Space: O(1)

            # Iterate through the stock prices:
                # If we already bought a stock, we presume we're going to make a profit by selling
                # here. 
                    # Therefore, sell the stock and add to profit.
                # Buy stock whenever the next stock price is higher than the current stock price.
                    # Mark that we bought a stock, so we can sell on the next iteration.
            
            bought = False
            profit = 0

            for i in range(len(prices)):
                if bought:
                    profit += prices[i]
                    bought = False

                if not bought and i < len(prices) - 1 and prices[i + 1] > prices[i]: 
                    profit -= prices[i]
                    bought = True

            return profit
