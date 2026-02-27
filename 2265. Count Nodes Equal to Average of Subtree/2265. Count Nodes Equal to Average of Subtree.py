#
# Problem: 2265. Count Nodes Equal to Average of Subtree
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-27


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0, 0
            leftsum, left = dfs(node.left)
            rightsum, right = dfs(node.right)

            cursum = node.val + leftsum + rightsum
            count = 1 + left + right

            if cursum//count == node.val:
                self.res += 1
            return cursum, count
        dfs(root)
        return self.res
