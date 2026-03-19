#
# Problem: 3212. Count Submatrices With Equal Frequency of X and Y
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description/?envType=daily-question&envId=2026-03-19
# Language: python3
# Date: 2026-03-19


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        prefixX = [0] * cols
        prefixY = [0] * cols
        res = 0

        for i in range(rows):
            rowx = 0
            rowy = 0
            for j in range(cols):
                if grid[i][j] == 'X':
                    rowx += 1
                elif grid[i][j] == 'Y':
                    rowy += 1
                # maintaining prefix sum for each row
                prefixX[j] += rowx 
                prefixY[j] += rowy
                if prefixX[j] > 0 and prefixX[j] == prefixY[j]:
                    res += 1
        return res
