#
# Problem: 346. Moving Average from Data Stream
# Difficulty: Easy
# Link: https://leetcode.com/problems/moving-average-from-data-stream/submissions/1904826097/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-01


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.list1 = []

    def next(self, val: int) -> float:
        self.list1.append(val)
        return sum(self.list1[-self.size:])/min(self.size, len(self.list1))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
