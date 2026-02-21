#
# Problem: 973. K Closest Points to Origin
# Difficulty: Medium
# Link: https://leetcode.com/problems/k-closest-points-to-origin/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-21


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [] # k points in the heap would be min distance, others max distances would be poped out

        for x,y in points:
            dist = (x**2) + (y**2)

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, [x,y]))
            else:
                heapq.heappushpop(max_heap, (-dist, [x,y]))
        
        return [[x,y] for _,[x,y] in max_heap]

