#
# Problem: 92. Reverse Linked List II
# Difficulty: Medium
# Link: https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-22


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftprev = dummy
        cur = head

        for i in range(left - 1):
            leftprev, cur = cur, cur.next
        # I have left prev, I have the left = cur
        prev = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        
        leftprev.next.next = cur
        leftprev.next = prev
        return dummy.next

