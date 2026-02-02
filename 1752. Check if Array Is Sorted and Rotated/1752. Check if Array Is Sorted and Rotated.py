#
# Problem: 1752. Check if Array Is Sorted and Rotated
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-02


class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_num = sorted(nums)
        
        for rot in range(len(nums)):
            flag = True
            for i in range(len(nums)):
                if nums[(rot + i)%len(nums)] != sorted_num[i]:
                    flag = False
                    break
            if flag:
                return True
        
        return False
