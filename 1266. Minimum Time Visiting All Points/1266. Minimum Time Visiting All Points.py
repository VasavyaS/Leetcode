#
# Problem: 1266. Minimum Time Visiting All Points
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-time-visiting-all-points/submissions/1904951822/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-02


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            x, y = points[i]
            targetX, targetY = points[i + 1]
            time += max(abs(targetX - x), abs(targetY - y))
        return time

