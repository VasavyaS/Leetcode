#
# Problem: 57. Insert Interval
# Difficulty: Medium
# Link: https://leetcode.com/problems/insert-interval/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-19


class Solution:
    def insert(self, intervals: List[List[int]], newIntervals: List[int]) -> List[List[int]]:
        i = 0
        res = []
        n = len(intervals)

        while i < n and intervals[i][1] < newIntervals[0]:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newIntervals[1]:
            newIntervals = (min(intervals[i][0], newIntervals[0]), max(intervals[i][1], newIntervals[1]))
            i += 1
        res.append(newIntervals)

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
