#
# Problem: 3634. Minimum Removals to Balance Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-removals-to-balance-array/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-24


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = 0
        resLen = 0
        while j < n:
            while i < j and nums[j] > nums[i] * k: #shrink the window until the condition is not satisfied
                i += 1
            resLen = max(resLen, (j - i+ 1)) #max len --> min deletions
            j += 1
        return n - resLen
