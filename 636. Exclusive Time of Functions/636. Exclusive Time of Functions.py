#
# Problem: 636. Exclusive Time of Functions
# Difficulty: Medium
# Link: https://leetcode.com/problems/exclusive-time-of-functions/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-21


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_time = [0]*n
        prev_start = 0
        call_stack = []

        for log in logs:
            job, func, time = log.split(':')
            
            jobid = int(job)
            timestamp = int(time)

            if func == 'start':
                if call_stack:
                    exclusive_time[call_stack[-1]] += timestamp - prev_start
                call_stack.append(jobid)
                prev_start = timestamp
            else:
                exclusive_time[call_stack.pop()] += timestamp - prev_start + 1
                prev_start = timestamp + 1
            
        return exclusive_time
