#This problem is a linked list problem, which tend to be a lot easier than other data structures due to how simple they are. Nodes only have..
#..few attributes, which in this case are the "value" attribute and the "next" attribute. So, for this problem, we create two variables, slow and fast.
#These names are derived from the Two Pointer Approach. This works by having a node that traverses twice as fast as the other node. We'll know if a cycle..
#..exists if the two variables point to the same node at any moment, meaning that a cycle does exist somewhere in the list.

#Time complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        # Traverse the list with two pointers
        while fast and fast.next:                   # Note: the reason that this is fast and fast.next is because we just want to make sure fast.next is not None ...
            slow = slow.next          # Move slow pointer by 1 step                                            ... so we dont call None.next from fast.next.next
            fast = fast.next.next     # Move fast pointer by 2 steps
            
            # If slow and fast meet, there's a cycle
            if slow == fast:
                return True
        
        # If we exit the loop, there's no cycle
        return False

#EX: [1,2,3,4], assume the loop goes from 4 to 1.

#Step 1: The slow pointer is at the node after the head (2). The fast pointer is at 3.
#Step 2: The slow pointer is now at 3, while the fast pointer is at 1, since after 4 is loops back to 1.
#Step 3: The slow pointe is now at 4, and the fast pointer is now at 3.
#Step 4: The slow pointer is at 1, and the fast pointer is at 1. The two are equal, so we return true.
        