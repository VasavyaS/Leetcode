#
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/description/
# Language: python3
# Date: 2026-01-11


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0


        for n in numset:
            if n - 1 not in numset:
                cur = n
                cur_str = 1

                while cur + 1 in numset:
                    cur += 1
                    cur_str += 1
                longest = max(longest, cur_str)
        return longest
# O(n) O(n)
