#include<bits/stdc++.h>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void printLinkedList(ListNode* head){
	while(head){
		cout << head->val << ' ';
		head = head->next;
	}
	cout << endl;
}
 
ListNode* oddEvenList(ListNode* head){
	if(!head || !head -> next)return head;
					
	// here I am initializing a to head & b to head->next
	ListNode *a = head;
	ListNode *b = head -> next;
	ListNode *temp = b;
	
	// traversing both and making two LLs to keep odd & even nodes
	while(a && a->next && b && b->next){
		a -> next = a -> next -> next;
		a = a -> next;
		if(a && a->next){
			b -> next = b -> next -> next;
			b = b -> next;
		}
	}
	
	// after one of them reaches NULL i am connecting end of 'a' to
	// start of 'b' (temp) and also terminating b with NULL
	a -> next = temp;
	b -> next = NULL;
	
	// finally returning head
	return head;
}	
	
int main(){
	ListNode d(4);
	ListNode c(3, &d);
	ListNode b(2, &c);
	ListNode a(1, &b);
	printLinkedList(oddEvenList(&a));
	return 0;
}