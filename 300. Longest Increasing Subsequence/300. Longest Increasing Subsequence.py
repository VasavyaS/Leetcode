#
# Problem: 300. Longest Increasing Subsequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-06


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
# longest till that number or 1 + previous positions

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
# O(n^2) O(n)
