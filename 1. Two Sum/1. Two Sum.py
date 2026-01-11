#
# Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/description/
# Language: python3
# Date: 2026-01-11


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            if target - n in hashmap:
                return [hashmap[target - n], i]
            hashmap[n] = i
        return 0
# O(n) O(n)
