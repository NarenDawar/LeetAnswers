#This problem can be done in another way without using hashmaps, but using a map (dictionary in Python) makes this problem a lot easier.
#This approach saves numbers and correlating indices in the list. So, as we iterate, we check if the current number is in our dictionary..
#..and if it is, we check if it's current index minus the index of the prior occurrence is <= k. If so, we can immediately return True.
#If the number isn't in our dictionary, we simply add it & it's index to the dictionary. Indices are also updated if i - num_indices[unum] > k.

#Time complexity: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Dictionary to store the last index of each number.
        num_indices = {}
        
        # Iterate through the array.
        for i, num in enumerate(nums):
            # Check if the number has been seen before.
            if num in num_indices:
                # Check if the difference between indices is <= k.
                if i - num_indices[num] <= k:
                    return True
            
            # Update the index of the current number.
            num_indices[num] = i
        
        # Return False is nothing found.
        return False

#EX: nums = [1,0,1,1], k = 1

#Step 1: Index 0, value of 1, is not already in the dictionary (hashmap), so we add it to the dictionary.
#Step 2: Index 1, value of 0, is not already in the dictionary, so we add it.
#Step 3: Index 2, value of 1, is already in the dictionary, so we check if abs(index1 - index 2) <= k. So 2 - 0 is 2, which isn't <= k, so we update..
#..the index associated with the value of "1". The index is now 2.
#Step 3: Index 3, value of 1, is already in the dictionary with an index of 2, so we now check if abs(index1 - index2) <= k. 3 - 2 is 1, which is..
#..<= 1, so this function will return true.