#
# Problem: 55. Jump Game
# Difficulty: Medium
# Link: https://leetcode.com/problems/jump-game/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-19


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i 
        
        return True if goal == 0 else False
