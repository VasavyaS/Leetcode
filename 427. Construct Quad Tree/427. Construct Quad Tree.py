#
# Problem: 427. Construct Quad Tree
# Difficulty: Medium
# Link: https://leetcode.com/problems/construct-quad-tree/description/?envType=company&envId=uber&favoriteSlug=uber-thirty-days
# Language: python3
# Date: 2026-05-10


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
#Quad Tree construction: The root itself doesn't have any value. We further divide only if the quadrant has different values.

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c): #pass the top left cell
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break
            if allSame: #leaf node
                return Node(grid[r][c], True)
            n = n//2
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c+n)
            bottomleft = dfs(n, r+n, c)
            bottomright = dfs(n, r+n, c+n)
            
            return Node(0, False, topleft, topright, bottomleft, bottomright)
        return dfs(len(grid), 0, 0)
