# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        # Traverse the list.
        while current and current.next: #Verify that the current node and next node do exist.
            if current.val == current.next.val:
                # Skip the next node if it's a duplicate. This is how we remove items in a Linked List.
                current.next = current.next.next
            else:
                # Move to the next node.
                current = current.next
                
        return head

#Linked Lists are a fairly straightforward data type, and although they can seem daunting, they have very few features (singly linked lists, at least).
#With a singly linked list, we have to consider a few things. First, we can reference the head node, which is how we start this process.
#Secondly, every node has a "value" and "next" aspect. The "value" aspect is simply what is inside the node, and the "next" aspect points to the next node.
#So, when we want to remove duplicates, if they're consecutive, you can change the current nodes next reference to point to the node after the next node.
#(current.next = current.next.next) changes the "next" valu of the node to point to the next next node, effectively removing the middle node between the two.

#Time complexity: O(1)

#EX: [1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5]
#When we start with this example, we start with the head node, which is the leftmost node. Then, while we have a current and next node that exist, we iterate.
#We see that the current.val is equal to current.next.val, so we set the "next" aspect of the head node to point to head.next.next, or node 3 (which is 2). We go through the loop..
#.. and do the same thing throughout. So, the repeating 3 will also disappear by changing the "next" part of the third node to point to the fifth node rather than the fourth.
#The result would be: [1 -> 2 -> 3 -> 4 -> 5]

#You may be wondering where the nodes that we drop go, and the answer is that they just go away. The memory that they took up is now free!
#You can envision it like a wooden stick. You can cut off certain parts and glue the remaining parts together. The parts you cut off are simply of no use.
