#
# Problem: 560. Subarray Sum Equals K
# Difficulty: Medium
# Link: https://leetcode.com/problems/subarray-sum-equals-k/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-20


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixsum = {0:1}
        cursum = 0

        for n in nums:
            cursum += n
            diff = cursum - k
            if diff in prefixsum:
                res += prefixsum[diff]
            prefixsum[cursum] = 1 + prefixsum.get(cursum, 0)
        return res
