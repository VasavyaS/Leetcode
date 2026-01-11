#
# Problem: Unknown Problem
# Difficulty: Medium
# Link: https://leetcode.com/problems/contains-duplicate/submissions/1881395953/
# Language: python3
# Date: 2026-01-11


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                return True
            hashmap[i] = 1
        return False
