#
# Problem: 162. Find Peak Element
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-peak-element/submissions/1908664701/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-05


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l= 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                return mid
