#
# Problem: 17. Letter Combinations of a Phone Number
# Difficulty: Medium
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1906405129/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-03


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []

        def backtrack(comb, i):
            if len(comb) == len(digits):
                res.append(comb)
                return
            for j in hashmap[digits[i]]:
                backtrack(comb+j, i+1)
        backtrack("", 0)
        return res
