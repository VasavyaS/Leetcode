#
# Problem: 269. Alien Dictionary
# Difficulty: Hard
# Link: https://leetcode.com/problems/alien-dictionary/description/?envType=company&envId=uber&favoriteSlug=uber-three-months
# Language: python3
# Date: 2026-05-20


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word} #adjacency list

        print(adj)

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1] #consider 2 words
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: #given condition; smaller word should come before the larger word
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]: # first char that is different
                    adj[w1[j]].add(w2[j])
                    break
        print(adj)
        visited = {} # False for visited; True for cycle in the path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True # currently visiting

            for nei in adj[char]:
                if dfs(nei):
                    return True # cycle detected because visited = true
            
            visited[char] = False # already been processed
            res.append(char)

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
