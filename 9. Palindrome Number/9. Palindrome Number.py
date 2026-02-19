#
# Problem: 9. Palindrome Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/palindrome-number/
# Language: python3
# Date: 2026-02-19


class Solution:
    def isPalindrome(self, x: int) -> bool:
        newNum = 0
        if x < 0:
            return False
        num = x
        while num != 0:
            last = num%10
            num = num//10
            newNum = newNum * 10 + last
        if newNum == x:
            return True
        return False
