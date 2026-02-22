#
# Problem: 1004. Max Consecutive Ones III
# Difficulty: Medium
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-22


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1
