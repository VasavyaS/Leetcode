#
# Problem: 863. All Nodes Distance K in Binary Tree
# Difficulty: Medium
# Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-21


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parent(node, parent):
            if node:
                node.parent = parent
                add_parent(node.left, node)
                add_parent(node.right, node)
        add_parent(root, None)
        visit = set()
        res = []

        def dfs(node, distance):
            if not node or node in visit:
                return
            visit.add(node)
            if distance == 0:
                res.append(node.val)
            dfs(node.parent, distance - 1)
            dfs(node.left, distance - 1)
            dfs(node.right , distance - 1)
        dfs(target, k)
        return res

