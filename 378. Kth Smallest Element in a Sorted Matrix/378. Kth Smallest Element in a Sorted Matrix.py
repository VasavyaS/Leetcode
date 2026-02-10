#
# Problem: 378. Kth Smallest Element in a Sorted Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-10


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []

        for i in range(len(matrix)):
            min_heap.append((matrix[i][0], i, 0))
        heapq.heapify(min_heap)
        
        elements = 0
        while elements < k:
            val, row, col = heapq.heappop(min_heap)
            if col + 1 < len(matrix):
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
            elements += 1
        return val
