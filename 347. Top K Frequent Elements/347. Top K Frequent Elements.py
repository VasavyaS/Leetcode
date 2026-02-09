#
# Problem: 347. Top K Frequent Elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-elements/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-09


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
# k is in the range [1, the number of unique elements in the array]
        freq = [[] for i in range(len(nums)+1)]

        for i, c in counter.items():
            freq[c].append(i)
        res = []
        
        for i in range(len(freq)-1, -1, -1):
            if freq[i]!=[] and k > 0:
                for j in freq[i]:
                    res.append(j)
                    k -= 1
        return res
