#
# Problem: 5. Longest Palindromic Substring
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-palindromic-substring/submissions/1906285382/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-03


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        i = 0

        for i in range(len(s)):
            l = i
            r = i

            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                    
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                    
                l -= 1
                r += 1
        return res

