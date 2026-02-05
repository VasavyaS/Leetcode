#
# Problem: 210. Course Schedule II
# Difficulty: Medium
# Link: https://leetcode.com/problems/course-schedule-ii/submissions/1908795270/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-05


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preadj = defaultdict(list)
        visit, cycle = set(), set()
        res = []

        for crs, pre in prerequisites:
            preadj[crs].append(pre)
        
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            visit.add(c)
            cycle.add(c)
            
            for pre in preadj[c]:
                if dfs(pre) == False:
                    return False
            cycle.remove(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
