#
# Problem: 1752. Check if Array Is Sorted and Rotated
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/1905126898/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-02


class Solution:
    def check(self, nums: List[int]) -> bool:
    # Check the adj elements, %n checks the circular condition. If it exists more than once return False
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] > nums[(i + 1)%n]:
                count += 1
            if count > 1:
                return False
        return True
# O(n) O(1)
