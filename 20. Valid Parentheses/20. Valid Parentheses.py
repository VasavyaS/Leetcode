#
# Problem: 20. Valid Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parentheses/submissions/1902589879/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-01-31


class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}
        stack = []

        for i in s:
            if i in '([{':
                stack.append(i)
                continue
            elif not stack or stack[-1] != hashmap[i]:
                return False
            stack.pop()
        
        return True if not stack else False            
