#
# Problem: 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/?envType=company&envId=uber&favoriteSlug=uber-three-months
# Language: python3
# Date: 2026-05-19


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = deque()
        minq = deque()
        l = 0
        ans = 0

        for r in range(len(nums)):
            while maxq and nums[r] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[r])
            
            while minq and nums[r] < minq[-1]:
                minq.pop()
            minq.append(nums[r])

            if maxq[0] - minq[0] > limit:
                if nums[l] == maxq[0]:
                    maxq.popleft()
                if nums[l] == minq[0]:
                    minq.popleft()
                l += 1
            ans = max(ans, r-l+1)
        return ans
