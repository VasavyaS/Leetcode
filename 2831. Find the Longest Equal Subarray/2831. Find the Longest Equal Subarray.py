#
# Problem: 2831. Find the Longest Equal Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-longest-equal-subarray/description/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-all
# Language: python3
# Date: 2026-05-03


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        positions = defaultdict(list)
        best = 0
        for i, n in enumerate(nums):
            positions[n].append(i)
        
        for idxs in positions.values():
            left = 0

            for right in range(len(idxs)):
                while (idxs[right] - idxs[left] + 1) - (right - left + 1) > k:
                    left += 1
                best = max(best, right - left + 1)
        return best

