#This problem is best solved by keeping track of the number of ways to get the the former steps and adding them up.
#For example, to find how many ways it takes to get to 4 steps, we would add the number of ways to get to 3 steps and the number of ways to get to 2 steps.
#This approach is used by the loop we have set. Remember that we want to find the result for n steps, so the second parameter should be n+1.
#We first check the two base cases, 1 and 2. After that, we set our previous values to 1 and 2, since this is where we start (starting at ways to reach step 3, which is 1+2 ways).
#In our loop, we set our current step equal to the two previous steps added (our overall approach), set our prev2 = prev1, and set our prev1 to current.
#Order here is important, since you should be changing the steps in order. If you change the wrong step, you'll get every answer wrong from after said step. 

#Time complexity: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize the base cases
        prev1, prev2 = 2, 1
        
        # Start calculating from the 3rd step to the nth step
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1

#EX: n = 4

#Step 1: Starting at 3, our first and second steps added are 3. So step 3 has 3 possibilities. Now, we step our prev1 to 3 and prev2 to 2.
#Step 2: We now get to step 4. Step 4 would be equal to num. of possibilities for step 2 + num. of possibilities for step 3. This would yield 5.
#Step 3: Though we stop at this step, our prev1 would now be 5 and prev2 would now be 3. So, the next step would have 5 + 3 options.