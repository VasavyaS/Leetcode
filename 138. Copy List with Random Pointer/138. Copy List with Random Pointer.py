#
# Problem: 138. Copy List with Random Pointer
# Difficulty: Medium
# Link: https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-10


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deepcopy = {None:None}
        cur = head

        while cur:
            copy = Node(cur.val)
            deepcopy[cur] = copy 
            cur = cur.next
        cur = head
        while cur:
            copy = deepcopy[cur]
            copy.next = deepcopy[cur.next]
            copy.random = deepcopy[cur.random]
            cur = cur.next
        
        return deepcopy[head]
