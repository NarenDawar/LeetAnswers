class Solution:
    def isPalindrome(self, x: int) -> bool: #Return type of boolean
        x1 = str(x) #Turn x into a string so we can iterate through it.
        x2 = x1[::-1] #The [::-1] literally means taking a number and reversing it.
        return x2 == x1 #Returns true/false based on if the number reversed is the same as the original.

#Python has a lot of useful features, and this is a simple example. The [:::] format represents [start:stop:step].
#So, in this instance, because there is no start or stop provided, it will by default consider the entire sequence, and -1 means to step backwards.
#Stepping backwards means it will start at the last index and go towards the first index.
        
