#
# Problem: 56. Merge Intervals
# Difficulty: Medium
# Link: https://leetcode.com/problems/merge-intervals/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-05


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]

        for i, j in intervals:
            lasti, lastj = res[-1]
            if i <= lastj:
                res[-1][1] = max(j, lastj)
            else:
                res.append([i, j])
        return res
    # O(n log n)
