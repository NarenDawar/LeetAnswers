#This code basically takes the first word in the list and continue reducing it until the prefix matches for all other words in the list.
#For example, if I had "flower", "flour", and "flow", the code would reduce flower -> flo because all words have the same prefix. 
# The .startswith() is a built in python function that checks if a word starts with a given string of characters or individual character.

#Time complexity: O(n * m) where n is the number of strings and m is the length of the shortest string in the array.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str: # Defining the return type.
        # Edge case: if the input list is empty, return an empty string.
        if not strs:
            return ""

        # Start by assuming the first string is the common prefix.
        prefix = strs[0]

        # Compare the prefix with each string in the list.
        for s in strs[1:]:
            # While the prefix is not a prefix of the current string, reduce it until the condition is met.
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                # If the prefix becomes empty, return an empty string.
                if not prefix:
                    return ""

        return prefix

#Example:
#Input: strs = ["flower", "flow", "flight"]

# First prefix would start as 'flower'.
# Next would would begin looking at 'flow' to see if it matches with 'flower', since it doesn't we truncate by 1 character each time until it matches. 'flower' -> 'flowe' -> 'flow'
# We end the 2nd iteration with 'flow' as our prefix
# In the last iteration we check if 'flight' matches with flow. Since it doesn't we truncate by 1 character each time until it matches. 'flow' -> 'flo' -> 'fl' 
#       NOTE: When we truncate the prefix we also check only up to the length of prefix. 
#        for example if our prefix is 'flow' and we check 'flight', we are really only checking if 'flow' and 'flig' match. 
#        Hence we use the .startsWith() function