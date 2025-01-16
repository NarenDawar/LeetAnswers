#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# The best way to solve this problem is to traverse the array backwards and keep track of the maximum value
# we've seen so far. We can then replace the current element with the maximum value we've seen so far.
# Except the last element, which we can replace with -1.

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        r = [0] * length
        m = arr[length-1]
        for i in range(length-2,-1,-1):
            r[i]=m
            m = max(m,arr[i])
        r[length-1]=-1
        return r
# Solution Link: https://www.youtube.com/watch?v=_CL3Dpi7KiM
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
