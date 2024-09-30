#This code revolves around making a dictionary in python that assigns values to strings.
#You simply reverse the string and traverse through while keeping track of the "previous value" variable.
#If the current value is less than the previous value, then we know that we must subtract the current value from the integer total.

#Time complexity: O(n)

class Solution:
    def romanToInt(self, s: str) -> int:
        # Map to assign value to characters.
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0  # To store the total integer value.
        prev_value = 0  # To keep track of the previous Roman numeral's value.
        
        # Iterate over the Roman string in reverse.
        for char in reversed(s):
            current_value = roman_map[char]  # Get the value of the current Roman numeral.
            
            # If the current value is less than the previous value, subtract it.
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value  # Otherwise, add the current value.
            
            # Update the previous value for the next iteration.
            prev_value = current_value
        
        return total


#EX: Inout: s = "III"
#    Output: 3
#    First you start at I; total = 1
#    Next you move to I, total = 1 + 1 = 2
#    Next you move to I, total = 2 + 1 = 3


#EX: Input: s = "MCMXCIV"
#    Output: 1994
#   First you start at V; total = 5
#   Next you move to I, however, since I is less than V, we subtract 1 from the total; total = 4
#   Next you move to C; total = 100 + 4 = 104
#   Next you move to X, however, since X is less than C, we subtract 10 from the total; total = 104 - 10 = 94
#   Next you move to M; total = 1000 + 94 = 1094
#   Next you move to C, however, since C is less than M, we subtract 100 from the total; total = 1094 - 100 = 994
#   Next you move to X, total = 994 + 1000 = 1994