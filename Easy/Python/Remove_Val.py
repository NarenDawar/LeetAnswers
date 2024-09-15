class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Initialize the pointer k for the non-val-equivalent elements.
        k = 0
        
        # Traverse the array.
        for i in range(len(nums)):
            # If the current element is not equal to val, move it to index k.
            if nums[i] != val:
                nums[k] = nums[i]  # Place the non-val element at index k.
                k += 1  # Move k to the next position.
        
        return k  # k is the count of elements not equal to val.

#This problem is kind of similar to the removing duplicates solution, or at least it holds the same premise.
#You iterate through the nums list, and if the current number doesn't equal the desired value to be removed, then set nums[k] to nums[i]. This allows us to replce gaps when we remove values.
#We also iterate k so that we can keep track of the number of elements that aren't equal to the desired value to be removed, since it must also be returned.

#Time complexity: O(n)

#EX: [1,3,4,7,2,4,3,6,4], val = 4
#Step 1: 1 != 4, so nums[0] = 1 (we basically just made it equal to 1 again), k = 1
#Step 2: 3 != 4, so nums[1] = 3 (we basically just made it equal to 3 again), k = 2
#Step 3: 4 == 4, so we simply skip over.
#Step 3: 7 != 4, so nums[2] = 7, and k = 3. Since we didn't iterate k earlier, we replaced that 4 with a 7. We now have two 7s, but they disappear after the next iteration.
#Step 4: 2 != 4, sp nums[3] = 2, and k = 4. Now the third index is 2, removing the duplicate 7.
#...continue until the end
