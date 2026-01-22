#
# Problem: 2380. Time Needed to Rearrange a Binary String
# Difficulty: Medium
# Link: https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/submissions/1892915034/?envType=company&envId=salesforce&favoriteSlug=salesforce-three-months
# Language: python3
# Date: 2026-01-22


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        time = 0
        zero = 0

        for c in s:
            if c == '0':
                zero += 1
            else:
                if zero > 0:
                    time = max(time+1, zero)
        return time
