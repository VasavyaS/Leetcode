#
# Problem: 2086. Minimum Number of Food Buckets to Feed the Hamsters
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/description/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-more-than-six-months
# Language: python3
# Date: 2026-05-04


class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        hamsters = list(hamsters)
        count = 0
        for i in range(len(hamsters)):
            if hamsters[i] == 'H':
                if (i-1) >= 0 and hamsters[i-1] == 'B': # 1. previous is a bucket
                    continue
                elif ((i+1) < n and hamsters[i+1] == 'H') or i == (n-1): # 2. next is H or end
                    if (i-1) >= 0 and hamsters[i-1] == '.':# 3. previous is empty
                        hamsters[i-1] == 'B'
                        count += 1
                        continue
                    else:
                        return -1
                elif (i+1) < n and hamsters[i+1] == '.':
                    hamsters[i+1] = 'B'
                    count += 1
                    continue
                else:
                    return -1
        return count

