#This approach works by going through each number in the list, subtracting it from the target number, and looking if that number is in the list.
#If that number isn't in the list, just store the current number and it's index into the seen dictionary, since it's a key-value pair.
#If you're wondering, enumerate allows you to keep track of the number of iterations. We use this because we are storing "i", the index. Enumerate starts at 0.

#Time complexity: O(n)

nums = []
target = "SOME_INTEGER"

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store the number and its index
        seen = {}
        
        # Loop through each element in the array.
        for i, num in enumerate(nums):
            # Calculate the complement.
            complement = target - num
            
            # If the complement is already in the dictionary, return the indices.
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, store the current number and its index
            seen[num] = i

#EX: [1,2,4,6,7], target : 10

#EX: [1,4,5,7,8,9]

#Step 1: 10 - 1 = 9, 9 isn't in the list, so this index-value pair is simply stored in the "seen" dictionary.
#Step 2: 10 - 2 = 8, 8 isn't in the list, so this pair is also added to "seen"
#Step 3: 10 - 4 = 6. 6 is in the list, so we simply return the indices of the two numbers that add up (seen[complement], i). The seen[complement] returns the index of the value of "complement" in the list, since...
#... our line seen[num] = i stores indices along with values.

#Reminder: Indices start at 0, not 1, in Python.




        