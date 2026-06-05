#
# Problem: 3584. Maximum Product of First and Last Elements of a Subsequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/description/?envType=company&envId=kla&favoriteSlug=kla-all
# Language: python3
# Date: 2026-06-05


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        maxleft, minleft = float('-inf'), float('inf')
        ans = float('-inf')

        for j in range(m-1, len(nums)):
            i = j - m + 1
            minleft = min(minleft, nums[i])
            maxleft = max(maxleft, nums[i])

            ans = max(nums[j]*minleft, nums[j]* maxleft, ans)
        
        return ans

