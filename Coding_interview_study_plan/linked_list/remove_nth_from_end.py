from linkedlist import ListNode
import linkedlist
from typing import Optional

def removeNthFromEnd(head: Optional[ListNode], n:int) -> Optional[ListNode]:
	dummy = ListNode(0, head)
	# Find nth
	node = dummy
	end = head
	for i in range(n):
		end = end.next
	
	while end:
		node = node.next
		end = end.next
	# Remove nth
	node.next = node.next.next

	return dummy.next

e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
head = ListNode(1, b)

n = 4
linkedlist.printList(removeNthFromEnd(head, n))