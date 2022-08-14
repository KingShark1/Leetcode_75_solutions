from linkedlist import ListNode
from typing import Optional

def printList(head : ListNode):
	while head:
		print(head.val)
		head = head.next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
	# Create a dummy node, store value of next in another dummy node, head should point to empty dummy node
	pre, cur = None, head
	while cur:
		pre, cur.next, cur = cur, pre, cur.next
	return pre

e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
head = ListNode(1, b)

printList(reverseList(head))