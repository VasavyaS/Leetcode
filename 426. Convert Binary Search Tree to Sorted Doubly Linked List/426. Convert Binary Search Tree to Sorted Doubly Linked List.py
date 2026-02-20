#
# Problem: 426. Convert Binary Search Tree to Sorted Doubly Linked List
# Difficulty: Medium
# Link: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-20


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        self.first = None
        self.last = None

        self.inorder(root)

        self.last.right = self.first
        self.first.left = self.last
        return self.first

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)

        if not self.last:
            self.first = node
        else:
            self.last.right = node
            node.left = self.last
        self.last = node
        self.inorder(node.right)
        return self.first
