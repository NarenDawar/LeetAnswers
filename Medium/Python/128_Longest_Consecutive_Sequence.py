# in order to find the largest conseq in O(n) time we cannot sequential search
# we need to find the start of a sequence and we can do that by checking if num-1 is not in the array( if it is that means that num is the middle of a seq)

# we can have O(1) look ups to check for this by converting the array to a set

# so we loop through the nums array and when we find a start numbers we use a while loop and iterate by 1 + num and keep a counter until we break the sequence

# this can happen multiple times so we keep a max 

# Time complexity: O(n)

#-------
# although its O(n) leetcode still had some TLE cases so i added a checked set to see which startNums we already seen and skip those in the future
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        checked = set()
        ret = 0
        for num in nums:
            if num-1 not in m and num not in checked:
                checked.add(num)
                cur = 1
                while num+cur in m:
                    cur+=1
                ret = max(ret, cur)
        return ret
                


        
