## [Remove nth element from end of a Linked List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
Logic : two pointers

- Initialize left node to begin from dummy node, and right node from head
- traverse "right" node by n nodes.
-	start traversing the Linked List, while right node is not null
- next element of left node is to be deleted, delete the node, return dummy.next.
