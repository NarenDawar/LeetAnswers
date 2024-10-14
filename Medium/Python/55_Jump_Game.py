#In this problem, it's important to remember that you only need 1 pathway that leads to the end of the list. So, we start by setting..
#..a variable that represents the max-reach of each index. We loop through by enumerating the list, meaning we can keep track of indices and values together.
#Our first check is if our index is greater than our max_reachable at any moment, because that means it's not possible to reach the end of the list (consider we get to the second to last index).
#After that check, we simply set max_reachable equal to either the current index + jump or the current max_reachable value. This is how we find the largest jumps.
#This may be hard to interpret based off explanation alone, but the example should help understand it better.

#Time complexity: O(n)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + jump)
        return True


#EX: [4,3,2,1]

#Step 1: max_reachable = 0, and now we start looping. Our first i, jump pair is 0, 4. 0 isn't > 0, so we don't return False. max_reachable is now 4 (0+4).
#Step 2: max_reachable = 4, now we start looping. Our next i, jump pair is 1, 3. 1 isn't > 4, so we continue. max_reachable is still 4, since it's max (4, 1+3).
#Step 3: max_reachable = 4, now we continue looping. Our next i, jump pair is 2, 2.  2 isn't > 4, so we continue. max_reachable is still 4.
#Step 4: max_reachable = 4, continue looping. Our next i, jump pair is 3, 1. 3 isn't > 4, so we continue. max_reachable stays at 4. The loop ends and we return true.
        