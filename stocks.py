def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0
    
    for price in prices:
        # Update the minimum price if a lower price is found
        if price < minPrice:
            minPrice = price
        # Calculate the maximum profit if we sell on the current day
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice
    
    return maxProfit

# Test case
prices = [7, 1, 5, 3, 6, 4]
maxProfitValue = maxProfit(prices)
print("Maximum Profit:", maxProfitValue)