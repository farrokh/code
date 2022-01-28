# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Say you have an array for which the ith element is the price of a given stock on day i.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# brute force solution. this will give timeout error.
# def maxProfit(prices):
#     maxProfit = 0
#     for i in range(len(prices)):
#         for j in range(i+1,len(prices)):
            # maxProfit = max(maxProfit,prices[j] - prices[i])
#      return profit


def maxProfit(prices):
    minNumber = prices[0]
    profit = 0
    for i,number in enumerate(prices):
        minNumber = min(minNumber, number)
        profit = max(profit,number-minNumber)
    return profit

# another solution:
    