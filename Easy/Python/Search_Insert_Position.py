class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Initialize left and right pointers.
        left, right = 0, len(nums) - 1
        
        # This algorithm is a binary search.
        while left <= right:
            mid = (left + right) // 2  # Calculate the mid-point.
            if nums[mid] == target:
                return mid  # Target found.
            elif nums[mid] < target:
                left = mid + 1  # Move the left pointer.
            else:
                right = mid - 1  # Move the right pointer.
        
        # If the target is not found, left will be the insertion position, since it's our variable for relativity.
        return left

#This approach uses binary search and adjusts the left and right boundaries to close in on the number. You have the right and left and..
#.. you use the middle value for incrementing them. Thinking about this from a logical standpoint helps with understanding. If you have a sorted..
#.. list and the middle value is greater than your target, then you need to adjust your right boundary to come down. If the middle number was lower, then you'd need to increase the left boundary.
#You essentially keep closing in using the right and left pointers until you find your number or the point where your number would be (the left <= right condition is when you'd get that number).

#Time complexity: O(log n)

#EX: [1,3,4,5,6,7,8], target = 2
#Step 1: Find mid, 0 + 6 //2 = 3, nums[3] is 5, 5 > 2, so right is now 2.
#Step 2: Find mid, 0 + 2 // 2 = 1, nums[1] is 3, 3 > 2, so right is now 0.
#Step 3: Find mid, 0 + 0 // 2 = 1, nums[0] is 1, 1 < 2, so left is now 1.
#Left is greater than right, so the loop ends there. Our left value is 1, and that's the index where we'd input 2, since it'd be between 1 and 3.

