#
# Problem: 12. Integer to Roman
# Difficulty: Medium
# Link: https://leetcode.com/problems/integer-to-roman/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-all
# Language: python3
# Date: 2026-05-25


class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]

        res = ""
        for sym, n in symList[::-1]:
            if num//n:
                count = num//n
                res += (count * sym)
                num = num%n
        return res
