#
# Problem: 219. Contains Duplicate II
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate-ii/
# Language: python3
# Date: 2026-02-19


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i,n in enumerate(nums):
            if n in hashmap and (i - hashmap[n]) <= k:
                return True
            hashmap[n] = i
        return False
