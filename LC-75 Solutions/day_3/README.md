## [Remove nth element from end of a Linked List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
Logic : two pointers

- Initialize left node to begin from dummy node, and right node from head
- traverse "right" node by n nodes.
-	start traversing the Linked List, while right node is not null
- next element of left node is to be deleted, delete the node, return dummy.next.

## [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
Logic : two pointers and reverse singly linked list

- initialize slow and fast pointers to head
- slow would go to next pointer and fast would go to next to next pointer, thus when fast = NULL or fast.next = NULL, slow would point to middle most element.
- reverse linked list begining from slow.
- check for palindrome.

#### Runtime 65.78% faster than the most
#### Memory Usage 73.39% lesser than the most