#
# Problem: 100. Same Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/same-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-22


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        return (self.isSameTree(p.left, q.left)and(self.isSameTree(p.right, q.right)))
