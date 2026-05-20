#
# Problem: 2858. Minimum Edge Reversals So Every Node Is Reachable
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/description/?envType=company&envId=uber&favoriteSlug=uber-thirty-days
# Language: python3
# Date: 2026-05-20


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append((v, 0))  # original direction, no reversal from u to v
            graph[v].append((u, 1))  # reverse direction, would need 1 reversal

        ans = [0] * n
        visited = set()

        # Count reversals needed when root = 0
        def dfs_count(node):
            visited.add(node)
            total = 0

            for nei, cost in graph[node]:
                if nei in visited:
                    continue
                total += cost
                total += dfs_count(nei)

            return total

        ans[0] = dfs_count(0)

        visited.clear()

        # Reroot answers
        def dfs_reroot(node):
            visited.add(node)

            for nei, cost in graph[node]:
                if nei in visited:
                    continue

                if cost == 0:
                    ans[nei] = ans[node] + 1
                else:
                    ans[nei] = ans[node] - 1

                dfs_reroot(nei)

        dfs_reroot(0)
        return ans
