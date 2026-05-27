#
# Problem: 317. Shortest Distance from All Buildings
# Difficulty: Hard
# Link: https://leetcode.com/problems/shortest-distance-from-all-buildings/description/?envType=company&envId=waymo&favoriteSlug=waymo-all
# Language: python3
# Date: 2026-05-27


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        min_dist = float('inf')
        dist_matrix = [[0] * cols for i in range(rows)]

        BUILDING = 1
        EMPTY = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == BUILDING:
                    local_dist = float('inf')
                    que = deque([(i , j , 0)]) #i, j, distance

                    while que:
                        r, c, dist = que.popleft()

                        for dr, dc in dirs:
                            if (r+dr) in range(rows) and (c+dc) in range(cols) and grid[r+dr][c+dc] == EMPTY:
                                grid[r+dr][c+dc] -= 1
                                dist_matrix[r+dr][c+dc] += dist + 1

                                que.append((r+dr, c+dc, dist + 1))
                                local_dist = min(local_dist,  dist_matrix[r+dr][c+dc] )
                        
                    EMPTY -= 1
                    min_dist = local_dist
        
        return min_dist if min_dist != float('inf') else -1
