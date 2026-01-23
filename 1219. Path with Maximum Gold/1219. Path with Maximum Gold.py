#
# Problem: 1219. Path with Maximum Gold
# Difficulty: Medium
# Link: https://leetcode.com/problems/path-with-maximum-gold/submissions/1894040157/?envType=company&envId=salesforce&favoriteSlug=salesforce-three-months
# Language: python3
# Date: 2026-01-23


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dir = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        max_gold  = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r, c))
            localmax_gold = 0
            for dr, dc in dir:
                localmax_gold = max(localmax_gold,  dfs(r+dr, c+dc))
            visit.remove((r,c))
            return localmax_gold + grid[r][c]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0 and (i, j) not in visit:
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold
