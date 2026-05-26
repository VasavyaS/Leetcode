#
# Problem: 239. Sliding Window Maximum
# Difficulty: Hard
# Link: https://leetcode.com/problems/sliding-window-maximum/description/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-all
# Language: python3
# Date: 2026-05-26


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        deq = deque()
        res = []

        while r < len(nums):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)

            if l > deq[0]:
                deq.popleft()
            if (r+1) >= k:
                res.append(nums[deq[0]])
                l += 1
            r += 1
        return res
        

