#
# Problem: 70. Climbing Stairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/climbing-stairs/submissions/1902596057/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-01-31


class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        if n==0 or n == 1:
            return 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
