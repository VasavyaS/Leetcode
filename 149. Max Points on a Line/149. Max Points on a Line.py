#
# Problem: 149. Max Points on a Line
# Difficulty: Hard
# Link: https://leetcode.com/problems/max-points-on-a-line/description/?envType=company&envId=waymo&favoriteSlug=waymo-all
# Language: python3
# Date: 2026-05-27


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
# count the points with a particular slope
        for i in range(len(points)):
            p1 = points[i]
            count = defaultdict(int)
            for j in range(i+1, len(points)):
                p2 = points[j]

                if p1[0] == p2[0]: # same x value
                    slope = float('inf')
                else:
                    slope = (p2[1] - p1[1])/(p2[0] - p1[0]) # (y2 - y1)/(x2 - x1)
                count[slope] += 1
            
                res = max(res, count[slope]+1)
        
        return res
# O(n^2)
