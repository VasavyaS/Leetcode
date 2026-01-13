#
# Problem: 3Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/3sum/description/
# Language: python3
# Date: 2026-01-13


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                triplet = nums[i] + nums[j] + nums[k]
                if triplet < 0:
                    j += 1
                elif triplet > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res
# O(n^2) O(n^2) or O(1)
