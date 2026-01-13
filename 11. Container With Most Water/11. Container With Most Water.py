#
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/description/
# Language: python3
# Date: 2026-01-13


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxAr = 0
        i = 0 
        j = len(height) - 1

        while i < j:
            area = (j - i) * min(height[i], height[j])
            maxAr = max(maxAr, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxAr

        
