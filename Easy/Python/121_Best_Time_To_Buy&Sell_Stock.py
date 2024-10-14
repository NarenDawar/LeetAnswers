#objective: use the array given to find the best time to buy and sell stock(cannot sell before you buy), then return max profit
    # prices = [7,1,5,3,6,4]; best time to buy is i = 1 and sell is i = 4, maxprofit = 6-1 = 5

# Min needs to be highest possible value to make sure that the first array value is set to min.
# Iterate through the prices array and compare min to current price to make sure you have the lowest price possible set to min and in turn the max profit..
# in the same loop calculate the profit from the min price to the current price you are looking at and decide whether that is greater than the max profit.
#If it is greater than maxprofit, then set that value to maxprofit.
# return maxprofit

#Time complexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        maxProfit = 0
        for price in prices:
            if(price < min):
                min = price
            profit = price - min
            if(profit > maxProfit):
                maxProfit = profit
        return maxProfit



#EX: [7,6,5,4]

#Step 1: Because the min is set at 7 and every number after that is decreasing, profit will always be negative, therefore maxProfit will always stay at 0
#                   return maxProfit (= 0)

#EX: [9,8,10]
#Step 1: After 2nd iteration min is set at 8 and last number is 10, when profit is calculated 10 - 8 = 2, so maxProfit = 2
#                   return maxProfit (= 2)