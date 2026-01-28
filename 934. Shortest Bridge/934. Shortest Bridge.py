#
# Problem: 934. Shortest Bridge
# Difficulty: Medium
# Link: https://leetcode.com/problems/shortest-bridge/description/?envType=company&envId=salesforce&favoriteSlug=salesforce-three-months
# Language: python3
# Date: 2026-01-28


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #Find one island and count how many steps to reach the other island.
        #DFS to find first island and BFS through layers until next island
        rows = len(grid)
        visit = set()
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        def invalid(r, c):
            if r not in range(rows) or c not in range(rows):
                return 1

        def dfs(r, c):
            if (invalid(r, c) or (r, c) in visit or grid[r][c] == 0):
                return 
            visit.add((r, c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
        
        def bfs():
            q = deque(visit)
            res = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        curR, curC = r + dr, c + dc
                        if (curR, curC) in visit or invalid(curR, curC):
                            continue
                        if grid[curR][curC] == 1:
                            return res
                        visit.add((curR, curC))
                        q.append([curR, curC])
                res += 1
        
        for r in range(rows):
            for c in range(rows):
                if grid[r][c] == 1:
                    dfs(r,c)
                    return bfs()
                        
