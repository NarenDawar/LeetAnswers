#This problem is very similar to the isomorphic strings problem. However, since we're comparing a pattern to words, we have to make split the string by words.
#Luckily, Python comes with a .split() function that allows us to split the words in a string and put them into a list. We can then iterate through the list.
#After this list is made, we iterate through the pattern string and for each character we check if key-value pairs exist and if the current mapping matches the recorded ones.

#Time complexity: O(n)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        my_dict = {} #Create a dictionary to store pairs.
        list_check = s.split() #Split the string by words (turns into a list).

        for i in range(len(pattern)):
            pattern_char = pattern[i] #Save the pattern character.
            list_word = list_check[i] #Save the current list word.

            if(pattern_char in my_dict): 
                if(my_dict[pattern_char] != list_word): 
                    return False #Return false if letter is mapped to different word already.
            else:
                my_dict[pattern_char] = list_word
        return True #Return true if you finish iterating and false is never thrown.

#EX: pattern: "abba", s: "dog cat cat dog"

#After splitting the list, we have a list with these elements: ["dog", "cat", "cat", "dog"]
#Step 1: Iterate through the string, we start at "a" and map it to "dog" and save it in our dictionary (i.e {"a":"dog"})
#Step 2: Now we get to "b" in the string and map it to "cat". This is saved in our dictionary.
#Step 3: We hit the second b and since it already exists in our dictionary, we check if the current mapping matches the dictionary one. It does, since both are "cat".
#Step 4: Lastly, we get to the final "a", and it already exists so we check if the current mapping matches the dictionary. Upon checking, they're the same, so this would return True.
        