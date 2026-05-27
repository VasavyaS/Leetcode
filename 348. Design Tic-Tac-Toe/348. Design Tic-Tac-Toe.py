#
# Problem: 348. Design Tic-Tac-Toe
# Difficulty: Medium
# Link: https://leetcode.com/problems/design-tic-tac-toe/description/?envType=company&envId=waymo&favoriteSlug=waymo-all
# Language: python3
# Date: 2026-05-27


class TicTacToe:
# row [0,0,0] col [0,0,0], dia = [0], antidia = [0]
# 1st move (001) - row [1 0 0] col [1 0 0] dia [1] 
# (022) - row [0 0 0]  col [1 0 -1] dia [1] antidia [-1]
# (221) - row [0 0 1] col [1 0 0] dia [2] anti [-1]
# (112) - row [0 -1 1] col [1 -1 0] dia [1] anti [-2]
# (201) - row [0 -1 2] col [2 -1 0] dia [1] anti [-1]
# (102) - row [0 -2 2] col [1 -1 0] dia [1] anti [-1]
# (211) - row [0 -2 3] col [1 0 0] dia [1] anti [-1] --> player 1

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.dia = 0
        self.antidia = 0     

    def move(self, row: int, col: int, player: int) -> int:
        score = 1 if player == 1 else -1

        self.rows[row] += score
        self.cols[col] += score

        if row == col :
            self.dia += score
        if row + col == self.n - 1:
            self.antidia += score
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.dia) == self.n or abs(self.antidia) == self.n:
            return player
        return 0

# O(1) O(n)

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
