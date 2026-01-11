#
# Problem: 242. Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram/submissions/1881594963/
# Language: python3
# Date: 2026-01-11


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if Counter(s) == Counter(t):
            return True
        return False
# O(n) O(26)
