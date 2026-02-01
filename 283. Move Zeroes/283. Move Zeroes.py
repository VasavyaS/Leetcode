#
# Problem: 283. Move Zeroes
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/submissions/1904183931/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-01


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 
        
        for r in range(len(nums)):
            if nums[r] != 0 :
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
        return nums

