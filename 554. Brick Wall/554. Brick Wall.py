#
# Problem: 554. Brick Wall
# Difficulty: Medium
# Link: https://leetcode.com/problems/brick-wall/description/?envType=company&envId=kla&favoriteSlug=kla-all
# Language: python3
# Date: 2026-06-08


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # finding max gap and then subtracting from the total len of rows --> gives min num of crossed bricks
        totalGap = {0:0}

        for row in wall:
            total = 0
            for b in row[:-1]:
                total += b

                totalGap[total] = 1 + totalGap.get(total, 0)
        return len(wall) - max(totalGap.values())

