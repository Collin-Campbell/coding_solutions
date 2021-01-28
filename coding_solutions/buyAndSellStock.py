"""

You are given the prices of a stock, in the form of an array of integers, 

prices. Let's say that prices[i] is the price of the stock on the ith day 

(0-based index). Assuming that you are allowed to buy and sell the stock 

only once, your task is to find the maximum possible profit (the difference 

between the buy and sell prices).

Note: You can assume there are no fees associated with buying or selling 

the stock.

"""

def buyAndSellStock(prices):
    max_profit = 0
    min_price = prices[0]
    for value in prices:
        if value < min_price:
            min_price = value
        if (value - min_price) > max_profit:
            max_profit = (value - min_price)
    
    return max_profit