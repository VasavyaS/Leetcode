#
# Problem: 680. Valid Palindrome II
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-palindrome-ii/submissions/1904897612/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-02


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                sleft = s[l:r]
                sright = s[l+1:r+1]
                return (sleft==sleft[::-1]) or (sright==sright[::-1])
            l += 1
            r -= 1
        return True

