#
# Problem: 3634. Minimum Removals to Balance Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-removals-to-balance-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-24


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        r = 0
        n = len(nums)
        ans = n

        for l in range(n):
            while r < n and nums[r] <= k * nums[l]:
                r += 1
            ans = min(ans,n-(r-l))
        return ans
