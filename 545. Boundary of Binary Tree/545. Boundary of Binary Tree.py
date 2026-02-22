#
# Problem: 545. Boundary of Binary Tree
# Difficulty: Medium
# Link: https://leetcode.com/problems/boundary-of-binary-tree/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-22


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def leftdfs(node): #pre-order
            if not node:
                return
            if not node.left and not node.right:
                return
            else:
                if node.left:
                    res.append(node.val)
                    leftdfs(node.left)        
                else:
                    res.append(node.val)
                    leftdfs(node.right)                  
        def findleaves(node):
            if not node:
                return
            if not node.right and not node.left:
                res.append(node.val)
            else:
                findleaves(node.left)
                findleaves(node.right)
        def rightdfs(node): #post-order
            if not node:
                return
            if not node.right and not node.left:
                return
            else:
                if node.right:
                    rightdfs(node.right)
                    res.append(node.val)             
                else:
                    rightdfs(node.left)
                    res.append(node.val)
        if not root:
            return []
        res.append(root.val)
        leftdfs(root.left)
        findleaves(root.left)
        findleaves(root.right)
        rightdfs(root.right)
        return res
# O(n) O(n)
