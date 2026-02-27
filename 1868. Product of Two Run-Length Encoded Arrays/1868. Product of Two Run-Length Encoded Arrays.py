#
# Problem: 1868. Product of Two Run-Length Encoded Arrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-27


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []

        while i < len(encoded1) and j < len(encoded2):
            i_val, i_freq = encoded1[i]
            j_val, j_freq = encoded2[j]

            prod = i_val * j_val
            freq = min(i_freq, j_freq)

            if res and res[-1][0] == prod:
                res[-1][1] += freq
            else:
                res.append([prod, freq])
            
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq

            if i_freq == freq:
                i += 1
            if j_freq == freq:
                j += 1
        
        return res
