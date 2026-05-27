#
# Problem: 939. Minimum Area Rectangle
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-area-rectangle/description/?envType=company&envId=waymo&favoriteSlug=waymo-all
# Language: python3
# Date: 2026-05-27


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_size = float('inf')
        visit = set()

        for x1, y1 in points:
            for x2, y2 in visit:
                if (x1, y2) in visit and (x2, y1) in visit:
                    size = abs(x2 - x1) * abs(y2 - y1)
                    min_size = min(min_size, size)
                
            visit.add((x1, y1))
        
        return min_size if min_size != float('inf') else 0
