#
# Problem: 347. Top K Frequent Elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-elements/description/
# Language: python3
# Date: 2026-01-11


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        counter = Counter(nums)

        for i, c in counter.items():
            freq[c].append(i)
        res = []
        for i in range(len(freq)-1, -1, -1):
            if freq[i] and k > 0:
                for n in freq[i]:
                    res.append(n)
                    k -= 1
        return res

