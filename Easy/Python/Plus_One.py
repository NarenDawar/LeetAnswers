class Solution:
    def plusOne(self, digits):
        # Start from the last digit and move left (because -1 step).
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits #Returns the edited list if the last number is 8 or less since the maximum possible result would be 9.
            digits[i] = 0  # Set current digit to 0 if it's 9.

        # If all the digits were 9, we need to add a leading 1.
        return [1] + digits

#This problem isn't too hard to solve as long as you work from the back to the front. We use a range of 0 to length - 1 since that would be the last possible index.
#We use -1 twice, the first one represents the finishing point, and the other represents the steps. -1 steps means that we work backwards.
#Whenever we reach a digit less than 9, we add one and return the list, since that would be the last addition necssary. Otherwise, we set it to 0, since 1 + 9 = 10, meaning we'd have to add that 1 to the next element.
#Here's an example:

#Time complexity: O(n)

# [1,2,3,4,5]
#Step 1: Starting from 5, we add 1, and since it's less than 9, we simply stop there. So, we return [1,2,3,4,6]

# [1,2,9,9]
#Step 1: Starting from 9, we add 1, and since it's now 10, we set it to zero and add the 1 to the next element.
#Step 2: On the next 9, we add 1, and since it's now 10, we set it to zero and add the 1 to the next element.
#Step 3: We end up on 2, and 2 + 1 is 3, so we end there since 2 < 9. Our result would be [1,3,0,0]


