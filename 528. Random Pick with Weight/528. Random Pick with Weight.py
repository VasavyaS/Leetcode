#
# Problem: 528. Random Pick with Weight
# Difficulty: Medium
# Link: https://leetcode.com/problems/random-pick-with-weight/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-21


class Solution:

    def __init__(self, w: List[int]):
        self.prefixsum = []
        self.total = 0

        for wei in w:
            self.total += wei
            self.prefixsum.append(self.total)

    def pickIndex(self) -> int:
        num = random.uniform(0, self.total)

        l = 0
        r = len(self.prefixsum)

        while l < r:
            mid =  (l+r)//2
            if num > self.prefixsum[mid]:
                l = mid + 1
            else:
                r = mid
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
