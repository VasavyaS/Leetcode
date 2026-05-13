#
# Problem: 252. Meeting Rooms
# Difficulty: Easy
# Link: https://leetcode.com/problems/meeting-rooms/description/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-more-than-six-months
# Language: python3
# Date: 2026-05-13


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prevEnd:
                return False
            prevEnd = end
        return True
#O(n log n)

