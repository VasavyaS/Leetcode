#
# Problem: 3Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/3sum/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-10


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        tri = []
        def ksum(k, start, target):
            if k != 2:
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    tri.append(nums[i])
                    ksum(k-1, i + 1, target - nums[i])
                    tri.pop()
                return
            l = start
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(tri+[nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        ksum(3, 0, 0)
        return res

# O(n^2) O(nlogn) or O(1)
