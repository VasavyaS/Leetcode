#
# Problem: 200. Number of Islands
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-islands/submissions/1908752449/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-05


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        count = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c]== '0':
                return
            visit.add((r,c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
            
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j] == '1':
                    count += 1
                dfs(i, j)
        return count
