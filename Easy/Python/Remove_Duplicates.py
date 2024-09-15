class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Edge case check: if the array is empty.
        if not nums:
            return 0
        
        # Initialize the pointer k for the unique elements.
        k = 1  # The first element is always unique.
        
        # Traverse the array starting from the second element.
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique.
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Place the unique element at index k.
                k += 1  # Move k to the next position.
        
        return k  # k is the count of unique elements.

#To solve this problem, we utilize a tracker, which is "k" in this case. In any instance where the current number doesn't equal the prior number, we move k up. 
#If the numbers are equal, then we keep the value of k, because k covers that duplicate, so we wait until we find another unique number to remove the duplicate since k covers the duplicate index.

#EX: [1,1,2,3,5,5]
#Step 1: k=1, nums[1] == nums[0], so nothing happens.
#Step 2: k=1, nums[2] != nums[1], so nums[k], which is nums[1], is now equal to nums[2]. K is now 2.
#Step 3: k=2, nums[3] != nums[2], so nums[k], which is nums[2], is now equal to nums[3]. K is now 3.
#This process repeats for the next indices. K is only incremented when unique values are found, so k returns 4 in this instance.
