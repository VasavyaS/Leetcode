#
# Problem: 692. Top K Frequent Words
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-words/description/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-more-than-six-months
# Language: python3
# Date: 2026-05-15


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        return [word for word,_ in sorted(counter.items(), key = lambda x: (-x[-1], x[0]))[:k]
        ]
