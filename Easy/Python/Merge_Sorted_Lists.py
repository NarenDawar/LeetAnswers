class ListNode:
    def __init__(self, val=0, next=None): #This is provided for us, defining a list node. Every node has a value and link to the next node.
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to serve as the head of the new merged list.
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists until one of them is exhausted.
        while list1 and list2:
            if list1.val < list2.val: #If the current node value of list1 < list2, then append list1 to current.
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2 #If the current node value of list2 < list1, then append list1 to current.
                list2 = list2.next
            # Move to the next node in the merged list after adding a node from either list1 or list2.
            current = current.next
        
        # If one list is exhausted, append the remaining nodes from the other list.
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list, starting from the node after the dummy (since it has no value).
        return dummy.next

#This approach utilizes a dummy starter node to make a new list. We traverse through both lists, comparing nodes and adding the smaller values first from either list.
#This approach is pretty simple and traverses two lists at once until one is exhausted, effectively adding all remaining values from the longer list to the new merged list, "current".

#Time complexity: O(n + m), where n & m are the number of nodes in list1 and list2, respectively.

#EX: [1,3,4,5] & [1,2,2,5,7]
#Step 1: Traversing through the first condition (list1.val < list2.val), 1 isn't less than 1, so we add the value from list, which is also 1.
#Step 2: Now comparing index 0 (1) from list and index 1 from list 2 (2), list1.val is less than list2.val, so we now add the other 1.
#Step 3: Comparing 3 & the second 2 from list2, list1.val isn't less than list2.val, so the second 2 is added to the "current" list.
#Step 4: Comparing 3 and 5, 3 is less than 5, so we add the 3 to the current list.
#...This pattern just follows throughout. List 1 gets exhausted first, so the remaining list 2 values (just 7) get appended to the "current" list in order as they show up in list2.
