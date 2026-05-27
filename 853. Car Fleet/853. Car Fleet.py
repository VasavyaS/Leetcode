#
# Problem: 853. Car Fleet
# Difficulty: Medium
# Link: https://leetcode.com/problems/car-fleet/description/?envType=company&envId=waymo&favoriteSlug=waymo-all
# Language: python3
# Date: 2026-05-27


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed))
        stack = []

        for p, s in pair[::-1]:
            stack.append((target - p)/s) #if the speed of the top is less that the previous, fleet is formed and they travel at the lower car's speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
