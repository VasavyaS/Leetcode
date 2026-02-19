#
# Problem: 205. Isomorphic Strings
# Difficulty: Easy
# Link: https://leetcode.com/problems/isomorphic-strings/description/
# Language: python3
# Date: 2026-02-19


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps_t = {}
        mapt_s = {}

        if len(s) != len(t):
            return False
        for c1, c2 in zip(s, t):
            if (c1 not in maps_t) and (c2 not in mapt_s):
                maps_t[c1] = c2
                mapt_s[c2] = c1
            elif maps_t.get(c1) != c2 or mapt_s.get(c2) != c1:
                return False

        return True
