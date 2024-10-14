#An intuitive approach to this problem is using binary search. We can use binary search by instantiating two values, 1 and x (the input).
#We calculate the midpoint of these values (1 and x) and see if that value times itself is less than, equal to, or greater than x.
#If the value we get is greater than x, then we decrement our right value by 1 since the current highest value is too high.
#If the value we get equals x, then we simply return that value since it's the exact square root of our x value.
#If the value is less then x, then we increase our left value by 1 since the minimum (left-most) value is too low.
#Remember that we calculate our mid values using left and right, so decrementing/incrementing these values does change the mid value we use for comparison.

#Time complexity: O(log n)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:  # Base case for x=0 and x=1, since 0^n and 1^n for any value n is 0 and 1 respectively.
            return x
        
        left, right = 1, x # Instantiate our values.
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid # Return mid if it's the exact answer.
            elif mid * mid < x:
                left = mid + 1
                ans = mid  # Store the current mid as the best candidate.
            else:
                right = mid - 1
        
        return ans  # Return the stored result.

#Reminder: // mean floor division. 5 / 2 is 2.5 but 5 // 2 rounds down to just 2.

#EX: x = 10

#Step 1: Calculate our midpoint, which is 1 + (10 - 1), which is just 10. When we floor divide that by 2, we get 5, which is our mid. 25 > 10, so we decrement our right pointer.
#Step 2: Our right is now 9 and our left is still 1. Our mid is now 1 + (9 - 1), which is 9. 9 // 2 is 4, and 4*4 = 16, which is > x, so we decrement our right again.
#Step 3: Our right is now 8 and our left is still 1. Our mid is 1 + (8 - 1), which is 8. 8 // 2 is 4, same deal as the last step. Decrement right again.
#Step 4: Our right is now 7, and our left is 1. Our mid stays at 7, 7//2 is 3, 3*3 is < x, so we save our answer as 3.
#From this step onwards we simply keep increasing our left pointer, and it'll pass our right pointer and end the loop. Our ans returned would be 3.
