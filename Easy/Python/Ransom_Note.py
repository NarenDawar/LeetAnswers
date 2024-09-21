class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        characters = {} #Dictionary for saving characters and number of occurence pairs.
        #
        for char in magazine: #Iterate through magazine and store all characters and number of times they occur.
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1

        # Iterate through the ransom note and check character counts to see if they match.
        for char in ransomNote:
            if char in characters and characters[char] > 0:
                characters[char] -= 1
            else:
                return False
        
        return True

#The approach to this problem is really easy using a dictionary (otherwise known as hash map in other languages). Dictionaries revolve around..
#..storing key value pairs, so in our case we're storing individual characters and number of times they show up in our magazine string.
#We return false in the instance that a character we encounter in "ransomNote" isn't in"magazine or if we have more of a character in ransomNote than magazine.
#We iterate through magazine first, create our key-value pairs, then iterate through remote and see if everything checks out.

#Time complexity: O(n * m)

#EX: magazine: "I am here", ransomNote: "hege"
#After iterating through the magazine text, our dictionary would be: {"I" : 1, "a" : 1, "m" : 1, "h" : 1, "e" : 2, "r" : 1}
#Then we'd iterate through the ransomNote by checking each character and verifying that it's in magazine and still has a value > 0.
#Hege has 1 H, 2 E's, and 1 G, and all the characters and values line us except for g, so this would return false.

