#
# Problem: 64. Minimum Path Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-path-sum/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-more-than-six-months
# Language: python3
# Date: 2026-05-14


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = [[float('inf')] * (cols + 1) for i in range(rows+1)]
        res[rows-1][cols] = 0

        for i in range(rows-1,-1,-1):
            for j in range(cols-1, -1, -1):
                res[i][j] = grid[i][j] + min(res[i+1][j], res[i][j+1])
        return res[0][0]
# DP. min for right and down. bottom up
