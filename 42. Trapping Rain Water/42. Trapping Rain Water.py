#
# Problem: 42. Trapping Rain Water
# Difficulty: Hard
# Link: https://leetcode.com/problems/trapping-rain-water/description/
# Language: python3
# Date: 2026-01-13


class Solution:
    def trap(self, height: List[int]) -> int:
# min(l, r) - h[i]
        l = 0
        r = len(height) - 1
        lMax = height[l]
        rMax = height[r]
        water = 0

        while l < r:
            if lMax < rMax:
                water += min(lMax, rMax) - height[l]
                l += 1
                lMax = max(lMax, height[l])
            else:
                water += min(lMax, rMax) - height[r]
                r -= 1
                rMax = max(rMax, height[r])
        return water
# O(n) O(1)
