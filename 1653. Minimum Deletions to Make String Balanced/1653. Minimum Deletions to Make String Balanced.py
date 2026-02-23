#
# Problem: 1653. Minimum Deletions to Make String Balanced
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-23


class Solution:
    def minimumDeletions(self, s: str) -> int:
        # b cannot occur before a 
        stack = []
        del_count = 0

        for ch in s:
            if stack and stack[-1] == 'b' and ch == 'a':
                stack.pop()
                del_count += 1
            else:
                stack.append(ch)
        return del_count
# O(n) O(n)
