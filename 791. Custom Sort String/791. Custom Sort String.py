#
# Problem: 791. Custom Sort String
# Difficulty: Medium
# Link: https://leetcode.com/problems/custom-sort-string/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-26


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        str_builder = []

        for c in order:
            str_builder.extend([c]*s_count[c])

            del s_count[c]
        
        for ch, count in s_count.items():
            str_builder.extend([ch]*count)
        
        return "".join(str_builder)

