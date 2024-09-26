#The solution to this problem involves using a dictionary and mapping values to one another. You progress through the length of one of the strings..
#..(they're the same so it doesn't matter what you pick) and we save both the character in s and character in t at the current index. Next, we have to check if..
#..s_to_t already has an entry with the letter we're on. In this case, we use s as the key pairs, but you can flip it, it doesn't matter. So we check for every character in s..
#.. to see if it's already in our dictionary, and if so, we have to check if the letter we're looking at is connected to the same character in the other string as..
#..stored in the dictionary. If it's linking to another character, then our function will return false. This problem is easier to see an example of than read.

#Time complexity: O(n)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): #Cannot be isomorphic if not same length.
            return False
        # Dictionaries for mapping.
        s_to_t = {}        

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            
            # Check if s_char is already mapped to another character.
            if s_char in s_to_t:
                if s_to_t[s_char] != t_char:
                    return False
            else:
                s_to_t[s_char] = t_char
            
        
        return True

#EX: s = "leader", t: "plerld"

#Step 1: Iterate through string s, first letter is 'l', it's not yet in our dictionary so we add it as a link to 'p'. {"l" : "p"} is stored.
#Step 2: We now go to 'e', it's not yet in our map, so we add it. {"e":"l"} is stored.
#Step 3: We now go to 'a', it's not yet in our map, so we add it. {"a":"e"} is stored.
#Step 4: We now go to 'd, it's not yet stored in our map, so we add it. {"d":"r"} is stored.
#Step 5: We now go to 'e', which we do actually have stored, so we check if the dictionary entry is equal to the t string character at the same index. Since the letter..
#..we stored is 'l' and the correlating letter at the same index is also 'l', our sample strings still pass.
#Lastly, we go to 'r', which we haven't yet stored as a key, so we add it to our dictionary. {"r":"d"}