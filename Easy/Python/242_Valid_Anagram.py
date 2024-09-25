#This problem is extremely easy to solve in python due to a given sorted() function. This function takes an iterable object..
#..like a list or string, and sorts the element in alphabetical / numerical order, depending on the data type.

#Time complexity: O(n log n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         # Step 1: Sort both strings.
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        # Step 2: Compare the sorted versions.
        return sorted_s == sorted_t

#EX: s = anagrams, t = gramanas

#When you sort these strings, they sort in alphabetical order since every piece of data is alphabetical. So, these two strings will be..
#..sorted alphabetically and compared, and since they have the same characters, they will be the exact same once sorted.