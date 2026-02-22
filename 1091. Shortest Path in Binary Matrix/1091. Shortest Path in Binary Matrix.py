#
# Problem: 1091. Shortest Path in Binary Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-22


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        que = deque([(0,0,1)])
        dirs = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]
        visit = set()

        while que:
            i,j,l = que.popleft()

            if i not in range(N) or j not in range(N) or grid[i][j] == 1:
                continue
            if i == (N - 1) and j == (N - 1):
                return l
            for dr, dc in dirs:
                if (i+dr, j+dc) not in visit:
                    que.append([i+dr, j+dc, l+1])
                    visit.add((i+dr, j+dc))
        
        return -1
# O(n) O(n)
