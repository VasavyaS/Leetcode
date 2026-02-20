#
# Problem: 71. Simplify Path
# Difficulty: Medium
# Link: https://leetcode.com/problems/simplify-path/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-20


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = path.split('/')

        for c in cur:
            if c == '..':
                if stack:
                    stack.pop()
            elif c == '.' or not c:
                continue
            else:
                stack.append(c)
        
        return '/'+'/'.join(stack)
            
