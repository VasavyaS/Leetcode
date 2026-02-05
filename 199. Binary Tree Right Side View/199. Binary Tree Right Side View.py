#
# Problem: 199. Binary Tree Right Side View
# Difficulty: Medium
# Link: https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-05


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, level):
            if not node:
                return 
            if len(res) < level:
                res.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
        dfs(root, 1)
        return res
            
