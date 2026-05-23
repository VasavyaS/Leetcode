#
# Problem: 102. Binary Tree Level Order Traversal
# Difficulty: Medium
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-all
# Language: python3
# Date: 2026-05-23


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        que = deque([root] if root else [])

        while que:
            level = []
            for i in range(len(que)):
                node = que.popleft()
                level.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(level)
        
        return res
