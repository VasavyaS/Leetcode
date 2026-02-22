#
# Problem: 1249. Minimum Remove to Make Valid Parentheses
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-22


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0

        for c in s:
            if c == '(':
                count += 1
                stack.append(c)
            elif c == ')' and count > 0:
                count -= 1
                stack.append(c)
            elif c != ')':
                stack.append(c)
        balanced = []

        for i in stack[::-1]:
            if i == '(' and count > 0:
                count -= 1
            else:
                balanced.append(i)
        
        return "".join(balanced[::-1])


