# The goal of this problem is to see what stones in the string 'stones' are both stones and jewels
# Stones and Jewels are both represented as characters in strings, where all jewels are unique but stones can repeat
# This is why we want to loop through stones because a stone can be just a stone or a stone AND a jewel and also because jewels are unique which might lead us to a smaller answer than expected

def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0  # keep track of no. of stones that are also jewels
        for stone in stones:
            if stone in jewels:  #checks is the current stone is in jewels
                count+=1
        return count

#Solution video: https://youtu.be/TGLAOGCDPzk

#Example cases:
#	Example 1:

#	Input: jewels = "aA", stones = "aAAbbbb"
#	Output: 3
#	Example 2:

#	Input: jewels = "z", stones = "ZZ"
#	Output: 0
