#
# Problem: 167. Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Language: python3
# Date: 2026-01-13


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            summ = numbers[i] + numbers[j]
            if summ == target:
                return [i+1, j+1]
            if summ > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]
# O(n) O(1)
