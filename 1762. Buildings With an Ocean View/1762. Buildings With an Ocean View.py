#
# Problem: 1762. Buildings With an Ocean View
# Difficulty: Medium
# Link: https://leetcode.com/problems/buildings-with-an-ocean-view/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-26


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []
        right_max = -1
        i = len(heights) - 1
        res = collections.deque([])

        while i >= 0:
            if heights[i] > right_max:
                res.appendleft(i)
                right_max = heights[i]
            i -= 1
        return list(res)
