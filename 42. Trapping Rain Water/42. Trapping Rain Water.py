#
# Problem: 42. Trapping Rain Water
# Difficulty: Hard
# Link: https://leetcode.com/problems/trapping-rain-water/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-24


class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        ans = 0

        while l < r:
            if lmax < rmax:
                ans += min(lmax, rmax) - height[l]
                l += 1
                lmax = max(lmax, height[l])
            else:
                ans += min(lmax, rmax) - height[r]
                r -= 1
                rmax = max(rmax, height[r])
        return ans

