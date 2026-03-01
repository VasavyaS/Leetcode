#
# Problem: 827. Making A Large Island
# Difficulty: Hard
# Link: https://leetcode.com/problems/making-a-large-island/?envType=company&envId=facebook&favoriteSlug=facebook-three-months
# Language: python3
# Date: 2026-03-01


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.island_id = -1
        self.island_area = {}
        
        self.dirs = [(0,1),(0,-1),(1,0),(-1,0)]

# 1. Calculate the area of the existing islands 
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    cur_area = self.dfs(grid, m, n)

                    self.island_area[self.island_id] = cur_area
                    self.island_id -= 1

# 2. Converting 0 to 1 and get the ids of the surrounnding islands and add the area. If the max_area is 0 then that means the grid is all 1, so return n*n
        max_area = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 0:
                    area = 1

                    surrounding_area = set()

                    for dr,dc in self.dirs:
                        new_m = m + dr
                        new_n = n + dc

                        if (0<= new_m < len(grid)) and (0 <= new_n < len(grid[0])) and grid[new_m][new_n] != 0:
                            surrounding_area.add(grid[new_m][new_n])
                        
                    for is_id in surrounding_area:
                        area += self.island_area[is_id]
                    
                    max_area = max(max_area, area)
        return max_area if max_area else len(grid)*len(grid[0])
    def dfs(self, grid, m, n):
        if (0 <= m < len(grid)) and (0 <= n < len(grid[0])) and grid[m][n] == 1:
            grid[m][n] = self.island_id
            area = 1

            for dr, dc in self.dirs:
                area += self.dfs(grid, m+dr, n+dc)
            
            return area
        else:
            return 0        
