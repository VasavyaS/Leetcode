#
# Problem: 496. Next Greater Element I
# Difficulty: Easy
# Link: https://leetcode.com/problems/next-greater-element-i/
# Language: python3
# Date: 2026-02-19


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = defaultdict(lambda:-1)

        for n in nums2:
            while stack and stack[-1] < n:
                hashmap[stack.pop()] = n
            stack.append(n)
        return [hashmap[i] for i in nums1]

