#
# Problem: 122. Best Time to Buy and Sell Stock II
# Difficulty: Medium
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# Language: python3
# Date: 2026-03-02


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit
