#This problem isn't very different from the first one, the only thing is that now we start from a different index and have a few more..
#..conditions to take into account.  In this problem, we start iterating from index 2, since every number can have at most 1 duplicate, so..
#..the first 2 indices (0 and 1) can be skipped because even if they are unique or identical, it is allowed. So, first we have a check for if the..
#..list is <= 2 in length, because then we can simply return the length of the list. Otherwise, we go through and compare the item at index j..
#..and the item at i-2. This is how we know when to iterate i, as you'll see the in the example below. If the values aren't equal, we set nums[i] = nums[j]..
#..and iterate i by 1. In the end, we simply return i since that counts the items in the array.

#Time complexity: O(n)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # If the array has 2 or fewer elements, no need to modify.

        # Initialize two pointers
        # `i` is the slow pointer, keeping track of the position for the next valid element
        # Start from index 2, because the first two elements are always allowed
        i = 2  

        for j in range(2, len(nums)):  # `j` is the fast pointer going through each element
            # Check if the current element at `j` is different from the element two positions back
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]  # Update the element at index `i`
                i += 1  # Move `i` to the next position

        return i  # `i` is the length of the array after removing duplicates

#EX: [1,1,1,2,2,3]

#Step 1: i = 2, j = 2, nums[j] (1) == nums[i-2] (1), so we skip everything in the loop.
#Step 2: i = 2, j = 3. nums[j] (2) != nums[i-2] (1), so nums[2] (ith position) is now 2 and i is now 3.
#Step 3: i = 3, j = 4, nums[j] (2) != nums[i-2] (1), so nums[3] (ith position) is now 2 and i is now 4.
#Step 3: i = 4, j = 5, nums[j] (3) != nums[i-2] (1), so nums[4] (ith position) is now 3, and i is now 5.

#Final list: [1,1,2,2,3,_]
#i = 5, so 5 is returned, which is correct since we have 1 empty space.
