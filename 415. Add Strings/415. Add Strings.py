#
# Problem: 415. Add Strings
# Difficulty: Easy
# Link: https://leetcode.com/problems/add-strings/submissions/1904880603/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-01


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        res = []

        while p1 >= 0 or p2 >= 0:
            n1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            n2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            val = n1 + n2 + carry
            carry = val//10
            res.append(val%10)
            p1 -= 1
            p2 -= 1
        
        if carry:
            res.append(carry)
        return ''.join(str(i) for i in res[::-1])


