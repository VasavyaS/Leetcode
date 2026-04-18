#
# Problem: 605. Can Place Flowers
# Difficulty: Easy
# Link: https://leetcode.com/problems/can-place-flowers/description/
# Language: python3
# Date: 2026-04-18


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if ( i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0) and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        if n <= 0:
            return True
        else:
            return False        
