#
# Problem: 670. Maximum Swap
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-swap/description/?envType=company&envId=facebook&favoriteSlug=facebook-three-months
# Language: python3
# Date: 2026-02-27


class Solution:
    def maximumSwap(self, num: int) -> int:
        que = deque([])
        
        while num != 0:
            que.appendleft(num%10)
            num = num//10
        
        i = len(que) - 1
        max_seen = que[i]
        max_idx = -1
        while i >= 0:
            cur = que[i]
            que[i] = (cur, max_seen, max_idx)
            if cur > max_seen:
                max_seen = cur
                max_idx = i
            i -= 1
        
        i = 0
        while i < len(que):
            num, mnum, midx = que[i]
            if num < mnum:
                que[i], que[midx] = que[midx], que[i]
                break
            i += 1
        num = 0
        for cur,_,_ in que:
            num = num*10 + cur
        
        return num


        
