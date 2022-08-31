class ListNode:
  def __init__(self, val=0, next=None):
    self.val = 0
    self.next = next

def printList(head : ListNode):
	while head.next:
		print(head.val)
		head = head.next

# Time complexity of both heap solution and merge solution are same, will just be implementing
# merge solution
def mergeKLists(lists):
	def mergeList(a, b):
			dummy = ListNode()
			tail = dummy
			while a and b:
					if a.val < b.val:
							tail.next = a
							a = a.next
					else:
							tail.next = b
							b = b.next
					tail = tail.next
			if a:
					tail.next = a
			if b:
					tail.next = b
			return dummy.next	

	if not lists or len(lists) == 0:
			return None

	while len(lists) > 1:
			mergedList = []
			for i in range(0, len(lists), 2):
					a = lists[i]
					b = lists[i+1] if (i+1) < len(lists) else None
					mergedList.append(mergeList(a, b))
			lists = mergedList
	return lists[0]

c = ListNode(4, None)
b = ListNode(2, c)
a = ListNode(1, b)

f = ListNode(5, None)
e = ListNode(0, f)
d = ListNode(-1, e)
lists = [a, b]
printList(mergeKLists(lists=lists))