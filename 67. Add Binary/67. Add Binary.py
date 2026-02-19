#
# Problem: 67. Add Binary
# Difficulty: Easy
# Link: https://leetcode.com/problems/add-binary/
# Language: python3
# Date: 2026-02-19


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        while y:
             # bitwise xor bitwise carry : and and left shift by 1. Has to be simulataneous assignement of x and y
            x, y = x^y, (x&y) << 1 
        return bin(x)[2:]
