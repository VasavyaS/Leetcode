#
# Problem: 169. Majority Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/majority-element/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-01


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        majority = max(counter.keys(), key = counter.get)
        return majority
