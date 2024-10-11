#The approach to this problem is really easy when you consider the given Python built-in functions. Rstrip() removes any trailing whitespaces and ...
#..split() takes a string of words and transforms it into a list where every index holds a word from the string. These two paired together do most of the work for you.
# All you have to do after that is check if the list does exist (meaning that there is at least one word/string of characters) and return length the last item in the list (which is -1 index).

#Time complexity: O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_string = s.rstrip().split() # rstrip() removes trailing whitespaces & split the string into separate words (empty strings not included)

        if new_string: # Check i any words are present
            return len(new_string[-1]) #Return the length of the last element of the new_string list.
        return 0 # Return 0 if the list is blank (all empty strings)
