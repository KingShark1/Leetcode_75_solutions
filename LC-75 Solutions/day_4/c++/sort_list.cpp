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

ListNode* getMid(ListNode* head){
	ListNode* mid = head;
	ListNode* fast = head->next;
	while(fast != NULL and fast->next != NULL){
		mid = mid->next;
		fast = fast->next->next;
	}
	return mid;
}

ListNode* merge(ListNode* left, ListNode* right){
	ListNode* dummy;
	ListNode* tail;
	dummy = tail;
	while(left and right){
		if (left->val < right->val){
			tail->next = left;
			left = left->next;
		}
		else{
			tail->next = right;
			right = right->next;
		}
		tail = tail->next;
	}
	if(left) tail->next = left;
	if(right) tail->next = right;
	return dummy->next;
}

ListNode* sortList(ListNode* head){
	if(head == NULL or head->next==NULL) return head;
	ListNode* left = head;
	ListNode* right = getMid(head);
	ListNode* tmp = right->next;
	right->next = NULL;
	right = tmp;

	left = sortList(left);
	right = sortList(right);
	return merge(left, right);
}
	
int main(){
	ListNode d(10);
	ListNode c(99990, &d);
	ListNode b(-19, &c);
	ListNode a(-4, &b);
	printLinkedList(merge(&a, &c));
	return 0;
}