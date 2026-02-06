#
# Problem: 287. Find the Duplicate Number
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-duplicate-number/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-06


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for n in nums:
            cur = abs(n)
            if nums[cur] < 0:
                return cur
                break
            nums[cur] = -nums[cur]
        return 
