#
# Problem: 41. First Missing Positive
# Difficulty: Hard
# Link: https://leetcode.com/problems/first-missing-positive/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-03-02


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [i for i in nums if i > 0]
        nums.sort()

        target = 1
        for n in nums:
            if n == target:
                target += 1
            elif n > target:
                return target
        return target
