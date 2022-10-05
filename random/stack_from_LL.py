class ListNode:
	def __init__(self, val=0, next=None) -> None:
		self.val = val
		self.next = next

[1, 2, 3, 4, 5]

def push_top(n, root):
	temp = ListNode(n, root)
	root = temp
	return root

def pop_top(root):
	temp = root.next 
	del root
	return temp


def print_top(root):
	print(root.val)


root = ListNode()
root = push_top(1, root)
root = push_top(2, root)
root = push_top(3, root)
root = pop_top(root)
print_top(root)