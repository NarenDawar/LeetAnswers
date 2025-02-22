# Essentially to get the most optimal solution with the least time complexity
# we go through the strs list and make an array for each of the values which represents the frequency of each character in the string
# This way each anagram will have the same array because the frequency of the characters are the same as long as the array is sorted alphabetically

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)          # defaultdict allows use to easy add values to a dict without checking if its already there

        for s in strs:      		 	# iterate through each string
            l = [0] * 26    		 	# make an char freq. array for all 26 characters
            for char in s:  		 	# go through each char in the string 
                l[ord(char) - ord('a')] +=1     # the index is going to be 0-26 alphabetically( explained better below)
            key = tuple(l)                      # dict keys have to be immutatble so we change the list -> tuple
            d[key].append(s)                    # finally for the list/tuple key we add the string to that list, the dict already knows its a list because we passed list as a param to defaultdict
        return list(d.values())                 # return



#Video solution: https://youtu.be/1kX3iXjoEuM

# EXPLANATION FOR CHAR INDEX
#   essentially lower case ascii values start at 97 ('a')
#   in order to turn this 97 to a 0 we need to subtract by the ascii value of 'a'
#   which is ord('a'), we do this for each char we iterate thru in order to get the index of array
