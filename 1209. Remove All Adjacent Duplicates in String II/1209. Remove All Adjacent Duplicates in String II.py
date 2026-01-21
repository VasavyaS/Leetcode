#
# Problem: 1209. Remove All Adjacent Duplicates in String II
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/?envType=company&envId=salesforce&favoriteSlug=salesforce-three-months
# Language: python3
# Date: 2026-01-21


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, count]

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        
        return ''.join(c * cnt for c,cnt in stack)
