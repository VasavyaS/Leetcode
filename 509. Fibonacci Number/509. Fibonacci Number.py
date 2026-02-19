#
# Problem: 509. Fibonacci Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/fibonacci-number/description/
# Language: python3
# Date: 2026-02-19


class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n+1):
            an = a + b
            a = b
            b = an
        return an
