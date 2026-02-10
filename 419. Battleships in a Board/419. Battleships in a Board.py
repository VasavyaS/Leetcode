#
# Problem: 419. Battleships in a Board
# Difficulty: Medium
# Link: https://leetcode.com/problems/battleships-in-a-board/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-10


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        visit = set()
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(r,c):
            if (r,c) in visit or r not in range(len(board)) or c not in range(len(board[0])) or board[r][c] == ".":
                return
            visit.add((r,c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
                      
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (i,j) not in visit:
                    count += 1
                    dfs(i,j)
        return count
