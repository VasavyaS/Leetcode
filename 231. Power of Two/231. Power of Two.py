#
# Problem: 231. Power of Two
# Difficulty: Easy
# Link: https://leetcode.com/problems/power-of-two/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-22


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==0:
            return False
        while n%2 == 0:
            n /= 2
        return (n == 1)
