#
# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-03-01


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        resLen = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) #remove the characters from the left until the characters stop repeating
                l += 1
            charSet.add(s[r])
            resLen = max(resLen, r-l+1)
            
        return resLen
# O(n) O(1)
