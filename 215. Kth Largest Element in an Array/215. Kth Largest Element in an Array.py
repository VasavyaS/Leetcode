#
# Problem: 215. Kth Largest Element in an Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-05


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                heapq.heappushpop(min_heap, n)
        
        return min_heap[0]

