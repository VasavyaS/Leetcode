#
# Problem: 443. String Compression
# Difficulty: Medium
# Link: https://leetcode.com/problems/string-compression/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-all
# Language: python3
# Date: 2026-05-25


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        newIdx = 0

        while i < len(chars):
            ch = chars[i]
            count = 1
            while (i+1) < len(chars) and chars[i+1] == ch:
                count += 1
                i += 1
            chars[newIdx] = ch
            newIdx += 1
            if count > 1:
                for c in str(count):
                    chars[newIdx] = c
                    newIdx += 1
            
            i += 1
        
        return newIdx
