#
# Problem: 8. String to Integer (atoi)
# Difficulty: Medium
# Link: https://leetcode.com/problems/string-to-integer-atoi/submissions/1906347881/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-03


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        i = 0
        sign = 1
        if len(s) == 0:
            return 0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i]== '+':
            sign = 1
            i += 1
        res = 0
        while i < len(s):
            if not s[i].isdigit():
                break
            res = res * 10 + int(s[i])
            i += 1
        res = sign * int(res)
        
        if res > 2**31 - 1:
            res = 2**31 - 1
        elif res < -2**31:
            res = -2**31
        return int(res)
