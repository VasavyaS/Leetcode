#
# Problem: 46. Permutations
# Difficulty: Medium
# Link: https://leetcode.com/problems/permutations/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-10


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack():
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            for i in nums:
                if i not in subset:
                    subset.append(i)
                    backtrack()
                    subset.pop()
        backtrack()
        return res
    # O(n!)
