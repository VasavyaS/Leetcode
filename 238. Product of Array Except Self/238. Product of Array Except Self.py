#
# Problem: 238. Product of Array Except Self
# Difficulty: Medium
# Link: https://leetcode.com/problems/product-of-array-except-self/description/
# Language: python3
# Date: 2026-01-11


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        
        for i in nums:
            res.append(prefix)
            prefix *= i
        postfix = 1
        for i in range(len(nums)-1, -1, -1):    
            res[i] *= postfix
            postfix *= nums[i]
        return res

# O(n) O(n)
