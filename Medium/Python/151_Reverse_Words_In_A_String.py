#This problem is relatively easy for a medium level problem. You start with creating a new string that you'll be returning and a list form of your string..
#..using .split(). This takes every word in your string and puts them into a list in the order they show up in within the string.
#After that, we must iterate through our list backwards and add each word. Additionally, we need to add whitespaces after each word in the list (except i=0).
#To accomplish the reverse traversal, we simply use the "reversed" function in python which allows for us to go from the end index to the start index.
#Within this loop, we add each list item to the newString, while also adding whitespaces if the index of the item isn't 0 in the list.
#We don't add a whitespace to the last element (i=0 since we go backwards) because our string will end up having an unnecessary/trailing whitespace, yielding the wrong answer.

#Time complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        newString = "" #New string.
        reverseString = s.split() #List of all words.

        for i in reversed(range(len(reverseString))): #Traverse the list backwards.
            if( i != 0): #Check if last index to avoid extra whitespace.
                newString += (reverseString[i] + " ")
            else:
                newString += reverseString[i]

        return newString #Return the newString we've been adding to.


#EX: "the sky is blue"
#Step 1: Use .split() to add each word into a list, saved as "reverseString". reverseString = ["the", "sky", "is", "blue"]
#Step 2: traverse through the list backwards. We add each item in the list to our currently blank newString.
#Step 3: From indices 1 -> 3, our string would look like "blue is sky". We add white spaces after adding words since .split() removes whitespaces.
#Step 4: For index 0, we simply add the word and don't add a whitespace, since a trailing whitespace would result.
#Step 5: Final result: "blue is sky the".

#Note: The whitespace check is important for getting the correct answer. Also remember that you can "add" strings using the + operator.