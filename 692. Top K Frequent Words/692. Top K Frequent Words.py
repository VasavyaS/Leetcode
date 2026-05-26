#
# Problem: 692. Top K Frequent Words
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-words/description/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-all
# Language: python3
# Date: 2026-05-26


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        res = []

        heap = [(-count, word) for word, count in counter.items()]
        heapq.heapify(heap)

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

