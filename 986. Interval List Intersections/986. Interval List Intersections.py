#
# Problem: 986. Interval List Intersections
# Difficulty: Medium
# Link: https://leetcode.com/problems/interval-list-intersections/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-26


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        intervals = []

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            if start1 > end2:
                j += 1
            elif start2 > end1:
                i += 1
            else:
                intervals.append([max(start1, start2), min(end1, end2)])
                if end2 > end1:
                    i += 1
                else:
                    j += 1
        
        return intervals
