#
# Problem: 34. Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1906477470/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-03


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def BinSer(leftbias):
            i = -1
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = (l+r)//2

                if target > nums[mid]:
                    l += 1
                elif target < nums[mid]:
                    r -= 1
                else:
                    i = mid
                    if leftbias:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i
        left = BinSer(True)
        right = BinSer(False)

        return[left, right]


