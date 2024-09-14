nums = []
target = "SOME_INTEGER"

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: #Set the return type to List.
        leng = len(nums) #Set the leng value for looping equal to the length of the array.
        for i in range(leng - 1): #Iterate through the entire array.
            for j in range(i + 1, leng): #Iterate from the ith position through the rest of the array.
                if (nums[i] + nums[j] == target): #Check if the two numbers add up to the target value during the current iteration.
                    return [i, j] #Return the two indices.
        return [] #Returns blank if no answer is found.

#This approach works by starting at the first index of the array and progressively going through and adding all other values
#..to find the solution. If it isn't found with the first element and any other element, then we start with the second number
#..in the array and try the numbers after that one by one. This approach prevents the code making unnecessary reptitions, since we've
#..already checked adding the ith value and all numbers before it.

#EX: [1,2,4,6,7], target : 10

#While i is in the first iteration, we check 1+2, 1+4, 1+6, 1+7. None of these are 10, so now we start at 2 (index = 1).
#Second i iteration: 2+4, 2+6, 2+7. None of these are 10, so now we start at 4 (index = 2).
#Third i iteration: 4+6, 4+7. Since 4+6 is 10, the loop would end there.

#Reminder: Indices start at 0, not 1, in Python.




        