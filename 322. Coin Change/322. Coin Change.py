#
# Problem: 322. Coin Change
# Difficulty: Medium
# Link: https://leetcode.com/problems/coin-change/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-20


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+ 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
