#
# Problem: 253. Meeting Rooms II
# Difficulty: Medium
# Link: https://leetcode.com/problems/meeting-rooms-ii/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-20


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0 
        s, e = 0, 0
        count = 0

        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res
# O(nlogn) O(n)
