#
# Problem: 314. Binary Tree Vertical Order Traversal
# Difficulty: Medium
# Link: https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-09


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        deq = deque()
        res = []
        deq.append([0,root])
        min_x, max_x = float('inf'), float('-inf')

        if not root:
            return []

        while deq:
            x, node = deq.popleft()
            hashmap[x] .append(node.val)
            min_x = min(x, min_x)
            max_x = max(x, max_x)

            if node.left:
                deq.append([x-1, node.left])
            if node.right:
                deq.append([x+1, node.right])
        
        for i in range(min_x, max_x+1):
            res.append(hashmap[i])
        
        return res


