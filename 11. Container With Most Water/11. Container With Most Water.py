#
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-26


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1

        while i < j:
            ar = (j - i) * min(height[j], height[i])
            max_area = max(max_area, ar)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
