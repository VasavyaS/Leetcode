#
# Problem: 888. Fair Candy Swap
# Difficulty: Easy
# Link: https://leetcode.com/problems/fair-candy-swap/submissions/1904924647/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-02


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        Sa, Sb = sum(aliceSizes), sum(bobSizes)
        B = set(bobSizes)

        for x in aliceSizes:
            y = ((Sb - Sa)//2) + x
            if y in B:
                return (x, y)
