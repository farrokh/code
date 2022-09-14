# Suppose you are given a list of integers, prices, that represent the price of Google's stock over time. prices[i] is the price of the stock on day i. You must buy the stock once and then later sell it. You are not allowed to sell before you buy.
# Write a function that returns an integer, which is the maximum profit you can make from buying the stock and then later selling it. If the list is empty, return 0.
# Example:
# prices = [10, 7, 5, 8, 11, 9]
# max_profit(prices) # returns 6
# # You buy the stock on day 2 for $5 and sell it on day 4 for $8. You make a profit of $3 - $5 = $6.
# prices = [10, 7, 5, 4, 3, 2]
# max_profit(prices) # returns 0
# # You can't make a profit because the stock price is always going down.
# prices = [10, 20, 30, 40, 50, 60]
# max_profit(prices) # returns 50
# # You buy the stock on day 0 for $10 and sell it on day 5 for $60. You make a profit of $60 - $10 = $50.
# prices = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]
# max_profit(prices) # returns 50

def max_profit(prices):
    # Write your code here
    return 0

# Solution
def max_profit(prices):
    # Write your code here
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    for i in range(1, len(prices)):
        current_price = prices[i]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)
    return max_profit



# Given an array of integers, return an array containing the integer that occurs the least number of times. If there are multiple answers, return all possibilities within the resulting array sorted in ascending order. When no solution can be deduced, return an empty array.

# Example:
# [10, 941, 13, 13, 13, 941]
# # 10 occurs once, 941 occurs twice, 13 occurs three times. 10 is the only integer that occurs once, so the answer is [10].
# [10, 941, 13, 13, 13, 941, 10]
# # 10 occurs twice, 941 occurs twice, 13 occurs three times. 10 and 941 both occur twice, so the answer is [10, 941].

def least_frequent(array):
    # Write your code here
    return array

# Solution
def least_frequent(array):
    # Write your code here
    if len(array) == 0:
        return []
    counts = {}
    for num in array:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    min_count = min(counts.values())
    return sorted([num for num in counts if counts[num] == min_count])
  


# sort an array:
# [1, 5, 2, 8, 3, 4]

def sort_array(array):
    # Write your code here
    return array

# Solution
def sort_array(array):
    # Write your code here
    array.sort()
    return array
