class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to simplify final list construction.
        dummy = ListNode()
        current = dummy
        carry = 0

        # Traverse both linked lists.
        while l1 or l2 or carry:
            # Get the current values, default to 0 if the list is exhausted.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of values and carry.
            total = val1 + val2 + carry
            carry = total // 10  # Update carry.
            digit = total % 10   # Get the current digit.

            # Create a new node with the calculated digit and attach to the result list.
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes in the input lists.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result list, starting from the node after the dummy.
        return dummy.next
