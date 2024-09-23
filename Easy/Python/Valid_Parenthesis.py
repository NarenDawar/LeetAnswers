class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets.
        p_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # A stack variable to keep track of opening brackets.
        stack = []

        # Iterate through each character in the string.
        for char in s:
            # Checks if the character is a closing bracket.
            if char in p_map:
                # Pop the top of the stack if it's not empty, otherwise use a filler. I chose p, you can put anything.
                top_element = stack.pop() if stack else 'p'

                # If the top element of the stack doesn't match the corresponding opening bracket, return False.
                if p_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack.
                stack.append(char)

        # After processing all characters, the stack should be empty.
        return not stack

# The way this works is you create a dictionary with key-value pairs. In this case, the keys are the closing brackets. 
#...This is important because we want to search for closing brackets, not opening ones (for this approach, but you could do either, it's just easier this way.)
#..This approach works by going through each value in the stack, looking for closing brackets (if p_map[char] = ...) and by popping the top of the stack to see if it correlates with the closing bracket found.
#..If the current character in the string isn't a closing bracket, then we push it to the stack, since it must be an opening bracket.

#Time complexity: O(n)

#EX: Imagine a string like so: "[{()]", the first three elements would be pushed to the stack, so the stack would look like "({[" (the last item pushed is the top of the stack, so "(" is the top of the stack). The first closing bracket is a normal parenthesis, and the top of the stack (which we pop) is also a normal parenthesis, so far so good.
# Now, the next parenthesis is a closing bracket ("]"). Now, if we pop the top of the stack, it's currently "{" (since we popped the "("), which doesn't correlate with the closing bracket, so this string would return false.
