#This problem can be solved by keeping track of i and i-1. You could also do i and i+1 but that would likely require a slightly altered approach.
#To attack this problem, we must create a new array, which in this case is ranges. We also have an edge case check for if the list is empty.
#For the problem, we iterate  through the list, and if the value at index i is not 1 + the value at index i+1, we append the start value -> i-1, since i is a jump >= 2.
#Keep in mind that the start variable iterates by 1 after an iteration in the for loop IF the number at index i is NOT equal to the number at index i-1 plus one.
#If start == the the value at i-1, then we simply append "start" since we never actually got to iterate i. For example, if we jump from 0 to 2, we jumped by >= 2..
#..so the start value was 0 and since there is no 1, we just append "0" with no arrow or final value.

#Time complexity: O(n)

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ranges = []
        
        # Edge case: If the input list is empty, return an empty list.
        if not nums:
            return ranges
        
        start = nums[0]
        
        for i in range(1, len(nums)):
            # If the current number is not consecutive to the previous one.
            if nums[i] != nums[i-1] + 1:
                # If start equals the previous number, it's one number.
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    # Otherwise, it's a range from start to the previous number.
                    ranges.append(f"{start}->{nums[i-1]}")
                
                # Update the start for the next range.
                start = nums[i]
        
        # After the loop, handle the last range or single number.
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{nums[-1]}")
        
        return ranges

#EX: [0,1,3,4,5,7]:

#Step 1: 0, start is now 0. No issues.
#Step 2: 1, start is still 0, 0 + 1 = 1, so no issues yet.
#Step 3: 3, start is still 0, 1 + 1 != 3, so we've run into an issue. Start != nums[i-1], so the else statement runs, and we append "0 -> 1". Start is now 3 (index 2).
#Step 4: 4, start is 3, 1 + 3 = 4, no issues found.
#Step 5: 5, start is still 3, 1 + 4 = 5, no issues.
#Step 6: 7, start is still 3, 5 + 1 != 7, so we now begin our checks. Start != nums[i-1], so the else statement executes, so we append "3 -> 5". Start is now 7.
#Step 7: We've approached the final value, so start = 7 and nums[-1] = 7 (nums[-1] is the last element). Since this condition is met, we simply append "7".

#Result: ["0->1", "3->5", "7"]