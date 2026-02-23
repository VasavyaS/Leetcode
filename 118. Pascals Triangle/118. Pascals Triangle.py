#
# Problem: 118. Pascal's Triangle
# Difficulty: Easy
# Link: https://leetcode.com/problems/pascals-triangle/
# Language: python3
# Date: 2026-02-23


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                add = temp[j] + temp[j+1]
                row.append(add)
            res.append(row)
        return res
    
    # Total element : O(numRows *(numRows + 1)/2) = O(numRows^2)
