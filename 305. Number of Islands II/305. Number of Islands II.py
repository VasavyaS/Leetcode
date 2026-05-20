#
# Problem: 305. Number of Islands II
# Difficulty: Hard
# Link: https://leetcode.com/problems/number-of-islands-ii/description/?envType=company&envId=uber&favoriteSlug=uber-three-months
# Language: python3
# Date: 2026-05-20


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        land = set()
        count = 0
        ans = []
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        def find(node):
            if parent[node]!= node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            pn1 = find(n1)
            pn2 = find(n2)
            
            if pn1 == pn2:
                return 0
            
            if rank[pn1] < rank[pn2]:
                parent[pn1] = pn2
            elif rank[pn2] > rank[pn1]:
                parent[pn2] = pn1
            else:
                parent[pn2] = pn1
                rank[pn1] += 1
            return 1
        
        for r,c in positions:
            if (r,c) in land:
                ans.append(count)
                continue
            
            land.add((r,c))
            parent[(r,c)] = (r,c)
            rank[(r,c)] = 0
            count += 1

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc

                if (nr,nc) not in land:
                    continue
                
                if union((r,c), (nr,nc)):
                    count -= 1
            ans.append(count)
        return ans
        
