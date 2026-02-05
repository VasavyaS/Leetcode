#
# Problem: 236. Lowest Common Ancestor of a Binary Tree
# Difficulty: Medium
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1908857920/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-05


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return
            if node.val == p.val or node.val == q.val:
                return node
            l = dfs(node.left)
            r = dfs(node.right)

            if l and r:
                return node
            return l or r
        
        return dfs(root)
