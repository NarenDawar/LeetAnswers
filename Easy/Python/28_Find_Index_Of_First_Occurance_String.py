#This approach simply gets the length of the two strings, and iterates through haystack in sub-portions to see if any of the partitions are equal to needle.
#This answer is pretty simple and there is a more efficient method: simply using the .find() method. This is a python function that will immediately just find the index of the occurrence.

#Time complexity: O(n*m)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Get the lengths of the haystack and needle variables.
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        # If needle is longer than haystack, then it can't be found.
        if needle_len > haystack_len:
            return -1
        
        # Iterate through each possible starting index in haystack (keep in mind the length of needle matters).
        for i in range(haystack_len - needle_len + 1):
            # Check if the substring from the current index matches needle.
            if haystack[i:i + needle_len] == needle:
                return i
        
        # If no match is found, return -1.
        return -1

#EX: haystack = "imnotmadbutsad" & needle = "sad"
#Step 1: i = 0, check if haystack[0:3] == needle, haystack[0:3] is imn, so this doesn't match.
#Step 2: i = 1, check if haystack[1:4] == needle, haystack[1:4] is mno, so this doesn't match.
#Step 3: i = 0, check if haystack[0:3] == needle, haystack[0:3] is not, so this doesn't match.
#....
#Eventually you get to "....sad", which returns a value of 11, since thats the value of i where haystack[i:i + needle_len] == "sad".

#Reminder: if I have a variable of var1 = "hello" and I return var1[0:3], this returns the characters at index 0, 1,and 2. The character at index 3 is NOT returned.