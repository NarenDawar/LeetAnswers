# The goal of this problem is to return a boolean whether the input string is a valid palindrome
# The string can have spaces and other characters but we are to only check the alphanumeric characters.
# Therefore a string can still be a palidrome if there are any invalid characters

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        s = s.lower()
        while(l < r):
            while not s[l].isalnum() and l < r:
                l+=1
            while not s[r].isalnum() and l < r:
                r-=1
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

#Leetcode 125: https://leetcode.com/problems/valid-palindrome/description/
#Video solution: https://youtu.be/pr_dyWk3aP8

#Example 1:

#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.
#Example 2:


#Input: s = "race a car"
#Output: false
#Explanation: "raceacar" is not a palindrome.
