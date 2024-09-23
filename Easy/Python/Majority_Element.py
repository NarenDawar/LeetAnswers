class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0 #Stores the highest repetition found from any one number.
        value = 0 #Stores the value most often found.

        for i in range(len(nums)): #First iterator
            count = 1
            for j in range(i+1, len(nums)): #Second iterator
                if (nums[i] == nums[j]):
                    count += 1
            if (count > max_count): #Checking if this count was greater than the highest count so far.
                value = nums[i]
                max_count = count
        return value

#To approach this problem, we need to have two variables, one that stores the highest number of repetitions and one that stores...
#..the number that has the highest number of repetitions. So, to start this problem, we make a first iterator that goes through the entire list. This is the first marker.
#Our second iterator is the second marker, and it iterates over every value after the first marker. This is how we are able to find the highest value and number of reps.
#Two important notes here are that after every loop of the first marker, you must reset count back to 1 because we're checking a new number.
#The other important thing is that after every single full loop, you have to check if the current count is greater than the highest recorded count. If so..
#..we replace the "max_count" variable with the current count, and we also record the value we were checking for during that loop as "value". In the end, we turn the "value" variable.

#Time complexity: O(n^2)

#EX: [1,2,3,4,4,5,6]:
#Step 1: First iterator is at 1 (index 0) and the second goes through 2,3,4,4,5,6. Count returned is 1, which is >0, so max_count is 1 and value is 1.
#Step 2: First iterator is at 2 (index 1) and the second goes through 3,4,4,5,6. Count returned is 1, which isn't >1, so max_count is 1 and value is 1.
#Step 3: First iterator is at 3 (index 2) and the second goes through 4,4,5,6. Count returned is 1, which isn't >1, so max_count is 1 and value is 1.
#Step 4: First iterator is at 4 (index 3) and the second goes through 4,5,6. Count returned is 2, which is >1, so max_count is 2 and value is 4.
#Step 5: First iterator is at 4 (index 4) and the second goes through 5,6. Count returned is 1, which isn't >1, so max_count is 2 and value is 4.
#..in the end, the value returned is 4 since it had the highest count (of 2).

        
        