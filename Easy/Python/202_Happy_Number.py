#This problem works by returning numbers in an endless loop or returning 1 eventually. In this problem we take a number and..
#..replace the number by the sum of the squares of its digits. We keep doing this and return True if 1 is returned or..
#..return False if a cycle is detected (this means a sum is created that we've already seen and is already present in the "seen" set).

#Time complexity: O(log n)

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() #Initialize a set.

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            
            # Calculate the sum of the squares of the digits.
            n = sum(int(digit) ** 2 for digit in str(n))
        
        return True

#EX: n = 19

#Step 1: 1^2 + 9^2 = 82 = num (1 and 9 are the digits of 19 so we square them both and add).
#Step 2: 8^2 + 2^2 = 68 = num (num is now 82, so the digits are 8 and 2, so we square them and add them.)
#Step 3: 6^2 + 8^2 = 100 = num (num is now 68, so the digits are 6 and 8, so we square them and add them.)
#Step 4: 1^2 + 0^2 + 0^2 = 1 = num -> 1 is reached so we return True.