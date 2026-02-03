#
# Problem: 22. Generate Parentheses
# Difficulty: Medium
# Link: https://leetcode.com/problems/generate-parentheses/submissions/1906489256/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-03


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(l, r, s):
            if len(s) == 2*n:
                res.append(s)
            if l < n:
                dfs(l+1, r, s+'(')
            if r < l:
                dfs(l , r+1, s+')')
        dfs(0, 0, "")
        return res
            
            
