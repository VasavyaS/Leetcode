#
# Problem: 443. String Compression
# Difficulty: Medium
# Link: https://leetcode.com/problems/string-compression/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-20


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        newidx = 0

        while i < len(chars):
            ch = chars[i]
            count = 1
            while (i+1) < len(chars) and chars[i+1] == ch:
                count += 1
                i += 1
            chars[newidx] = ch
            newidx += 1
            if count > 1:
                for c in str(count):
                    chars[newidx] = c
                    newidx += 1
            i += 1
        return newidx
# O(n) O(1)
