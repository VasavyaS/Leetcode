#
# Problem: 151. Reverse Words in a String
# Difficulty: Medium
# Link: https://leetcode.com/problems/reverse-words-in-a-string/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-04


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        return " ".join(words[::-1])
# O(n) O(n)
