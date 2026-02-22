#
# Problem: 1382. Balance a Binary Search Tree
# Difficulty: Medium
# Link: https://leetcode.com/problems/balance-a-binary-search-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-22


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
# Inorder the tree it gives increasing order list. Then balance it by recursively finding the mid.
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        def balance(arr, l, r):
            if l > r:
                return
            mid = (l+r)//2

            lSubTree = balance(arr, l, mid - 1)
            rSubTree = balance(arr, mid+ 1, r)

            node = TreeNode(arr[mid], lSubTree, rSubTree)
            return node

        inorder(root)
        return balance(arr, 0, len(arr)-1)
