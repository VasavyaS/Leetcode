#
# Problem: 77. Combinations
# Difficulty: Medium
# Link: https://leetcode.com/problems/combinations/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-22


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(idx):
            if len(subset) == k:
                res.append(subset[:])
                return
            for i in range(idx, n+1):
                subset.append(i)
                backtrack(i+1)
                subset.pop()
            
        
        backtrack(1)
        return res
