#
# Problem: 1101. The Earliest Moment When Everyone Become Friends
# Difficulty: Medium
# Link: https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/description/?envType=company&envId=uber&favoriteSlug=uber-thirty-days
# Language: python3
# Date: 2026-05-20


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

        logs.sort(key=lambda x: x[0])
        uf = UnionFind(n)
        groups = n

        for time, a, b in logs:
            if uf.union(a, b):
                groups -= 1
            if groups == 1:
                return time

        return -1


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1

        return True
