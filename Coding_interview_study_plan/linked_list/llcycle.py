from linkedlist import ListNode
from typing import Optional

def hasCycle(head: Optional[ListNode]) -> bool:
	# Floyd's version
	# fast = head
	# slow = head
	# while fast or slow:
	# 	fast = fast.next.next
	# 	slow = slow.next
	# 	if fast == slow: return True
		
	# return False
	while head:
		if head.val == None: return True
		head.val = None
		head = head.next
	return False

e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
head = ListNode(1, b)
e.next = c

print(hasCycle(head))