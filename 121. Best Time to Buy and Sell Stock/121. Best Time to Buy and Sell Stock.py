#
# Problem: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-01-31


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for i in prices:
            maxProfit = max(maxProfit, i - minPrice)
            minPrice = min(minPrice, i)
        return maxProfit
# O(n) O(1)
