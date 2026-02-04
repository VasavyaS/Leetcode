#
# Problem: 129. Sum Root to Leaf Numbers
# Difficulty: Medium
# Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-04


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sumR = 0

        def dfs(node, sumR):
            if not node:
                return 0
            
            sumR = sumR * 10 + node.val
            if not node.left and not node.right:
                return sumR
            
            return dfs(node.left, sumR) + dfs(node.right, sumR)
        
        return dfs(root, 0)
