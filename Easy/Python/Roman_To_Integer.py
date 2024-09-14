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
            
            # If the current value is less than the previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value  # Otherwise, add the current value
            
            # Update the previous value for the next iteration
            prev_value = current_value
        
        return total
