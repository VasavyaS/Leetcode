#
# Problem: 743. Network Delay Time
# Difficulty: Medium
# Link: https://leetcode.com/problems/network-delay-time/description/?envType=company&envId=salesforce&favoriteSlug=salesforce-three-months
# Language: python3
# Date: 2026-01-26


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, time in times:
            adj[u].append((v, time))

        min_heap = [(0, k)] # (time taken from source to node, node)
        visited = {}

        while min_heap:
            time_k_to_i, i = heapq.heappop(min_heap)

            if i in visited:
                continue
            visited[i] = time_k_to_i
            
            for nei, nei_time in adj[i]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time_k_to_i + nei_time, nei)) #time from source + cur time
        
        if len(visited) == n:
            return max(visited.values())
        else:
            return -1
