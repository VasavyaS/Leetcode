#
# Problem: 143. Reorder List
# Difficulty: Medium
# Link: https://leetcode.com/problems/reorder-list/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-26


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #First finding the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the 2nd half
        prev = None
        cur = slow.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        slow.next = None

        head1 = head
        head2 = prev
        while head2:
            tmp = head1.next
            head1.next = head2
            head1 = head2
            head2 = tmp
        return head
        
