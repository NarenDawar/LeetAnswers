class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 #Create a variable to track max profit.

        for i in range(len(prices)): #Iterator 1
            for j in range(i+1, len(prices)): #Iterator 2
                if(prices[j] - prices[i] > max_profit): 
                    max_profit = prices[j] - prices[i] #Change max_profit is larger value is found.
        return max_profit

#This problem is very similar to the majority element problem, following the idea of having two iterators and a variable for tracking.
#In this problem. we create a "max_profit" variable and create two iterators, one which is our starting and the other which checks all other values.
#We subtract the value at the first iterator index from the second iterator index since it's a buying & selling process, and the aim is to buy low and sell high.
#So, we essentially try subtracting all possible combinations that make sense, we cannot sell then buy, and find the largest profit available.
#We initialize the max_profit to zero in case the list is descending, because then there is no way for us to sell at a price higher than our buying price. The poblem..
#..prompts us to return 0 if there is no profit available, which is why we set it to zero.

#Time complexity: O(n)

#EX: [7,6,5,4]

#Step 1: First iterator is at 7 and second iterator goes through all other values. Subtractions checked: 6-7, 5-7, 4-7. None are greater than 0, so max_profit is 0.
#Step 2: First iterator is at 6 and second iterator goes through all other values. Subtractions checked: 5-6, 4-6. None are greater than 0, so max_profit is 0.
#..As you may have noticed, the listi is descending, so we'll never get a positive number, meaning there is no way for us to make profit.

#EX: [9,8,10]

#Step 1: First iterator is at 9 and second iterator goes through all other values. Subtractions checked: 8-9, 10-9. 10-9 is greater than 0, so max_profit is now 1 (10-9).
#Step 2: First iterator is at 8 and second iterator goes through all other values. Subtractions checked: 10-8. 10-8 is greater than 1, so max_profit is now 2 (10-8).
