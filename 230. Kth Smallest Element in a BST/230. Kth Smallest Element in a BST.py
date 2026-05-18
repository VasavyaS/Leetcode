#
# Problem: 230. Kth Smallest Element in a BST
# Difficulty: Medium
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=company&envId=uber&favoriteSlug=uber-three-months
# Language: python3
# Date: 2026-05-18


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res[k-1]

