#
# Problem: 1475. Final Prices With a Special Discount in a Shop
# Difficulty: Easy
# Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/?envType=company&envId=uber&favoriteSlug=uber-thirty-days
# Language: python3
# Date: 2026-05-10


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices[:]

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    break
        return answer
