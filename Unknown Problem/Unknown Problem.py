#
# Problem: Unknown Problem
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/submissions/1905159272/
# Language: python3
# Date: 2026-02-02


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def isSorted(nums):
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
            return True
        count = 0
        while not isSorted(nums):
            count += 1
            minSum = float('inf')
            i1, i2 = 0, 0
            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < minSum:
                    minSum = nums[i] + nums[i+1]
                    i1 = i
                    i2 = i+1
            nums = nums[:i1] + [minSum] + nums[i2+1:]
        
        return count
