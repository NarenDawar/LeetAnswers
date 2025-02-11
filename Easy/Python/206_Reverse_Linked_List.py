# This is a straight forward problem, given a linked list by its head we simply have
# to reverse the linked list

# So they way to approach it to iterate through and point the current node to the previous node
# then move to the next node and do the same thing, however, we need to make sure the keep the next
# node in scope so we don't just chop off the entire list


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head                     #start at head
        prev = None			#prev starts at None because nothing behind head
        while(curr):			#stop until current node is NULL
            temp = curr.next		# within the loop keep track of curr.next so we still have reference to it
            curr.next = prev		# now step current to previous
            prev = curr			# then move prev to current
            curr = temp			# curr now moves to the next node which we kept in temp so we do not lose it
        return prev			# by the end of the process, curr will be null and prev will be the first/head node

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
