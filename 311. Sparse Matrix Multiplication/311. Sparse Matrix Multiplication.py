#
# Problem: 311. Sparse Matrix Multiplication
# Difficulty: Medium
# Link: https://leetcode.com/problems/sparse-matrix-multiplication/submissions/1912943556/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-09


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat1[0])):
                    if mat1[i][k] != 0 and mat2[k][j] !=0:
                        res[i][j] += mat1[i][k] * mat2[k][j]
        
        return res
