#include <bits/stdc++.h>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* removeNthFromEnd(ListNode* head, int n){
	// Initialize step
	ListNode dummy(0, head);
	ListNode* right = head;
	ListNode* left = &dummy;
	
	while(n > 0 and right != NULL){
		right = right->next;
		n -= 1;
	}
	while(right != NULL){
		left = left->next;
		right = right->next;
	}

	// Delete Step
	left->next = left->next->next;
	return dummy.next;
}

int main(){
	ListNode c(1);
	ListNode b(2, &c);
	ListNode a(1, &b);
	int n = 2;
	cout<<removeNthFromEnd(&a, n)<< endl;
	return 0;
}