class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def printList(head : ListNode):
	while head:
		print(head.val)
		head = head.next