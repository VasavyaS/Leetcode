#
# Problem: Unknown Problem
# Difficulty: Medium
# Link: https://leetcode.com/problems/reverse-integer/submissions/1906287874/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-03


class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        rev = 0

        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev if x >= 0 else -(rev)
