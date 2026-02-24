#
# Problem: 987. Vertical Order Traversal of a Binary Tree
# Difficulty: Hard
# Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/submissions/1929461624/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-24


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        que = deque([(root, 0, 0)])
        xmin = float('inf')
        xmax = float('-inf')
        res = []

        while que:
            node, r, c = que.popleft()
            hashmap[c].append((node.val, r)) #{0: [[3, 0]]}
            xmin = min(xmin, c)
            xmax = max(xmax, c)

            if node.left:
                que.append((node.left, r+1, c-1))
            if node.right:
                que.append((node.right, r+1, c+1))
            
        for x in range(xmin, xmax+1):
            items = hashmap[x]
            items.sort(key = lambda x: (x[1], x[0]))
            items = [i for i, _ in items]
            res.append(items)
        return res

