#
# Problem: 50. Pow(x, n)
# Difficulty: Medium
# Link: https://leetcode.com/problems/powx-n/submissions/1907606666/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-04


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(x, n):
            if x == 1 or n == 0:
                return 1
            if x == 0:
                return 0
            
            res = power(x, n//2)
            res = res * res
            return res * x if n % 2 else res
        
        res = power(x , abs(n))
        return res if n > 0 else (1/res)
