#
# Problem: 2380. Time Needed to Rearrange a Binary String
# Difficulty: Medium
# Link: https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/description/?envType=company&envId=salesforce&favoriteSlug=salesforce-three-months
# Language: python3
# Date: 2026-01-22


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count = 0

        while '01' in s:
            s = s.replace('01', '10')
            count += 1
        return count

# O(n^2) O(n)
