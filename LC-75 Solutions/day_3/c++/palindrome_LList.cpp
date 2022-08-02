#include <bits/stdc++.h>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

bool isPalindrome(ListNode* head){
	ListNode* slow = head;
	ListNode* fast = head;

	// Finding middle (slow gets to middle)
	while(fast and fast->next){
		fast = fast->next->next;
		slow = slow->next;
	}

	// Reverse 2nd half
	ListNode* prev(0);
	ListNode* tmp(0);
	while(slow){
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}

	// Check Palindrome
	ListNode* left = head;
	ListNode* right = prev;
	while(right){
		if (left->val != right->val) return false;
		left = left -> next;
		right = right-> next;
	}
	return true;
}

int main(){
	ListNode c(1);
	ListNode b(2, &c);
	ListNode a(1, &b);
	cout << isPalindrome(&a) << endl;
	return 0;
}
 