#
# Problem: 408. Valid Word Abbreviation
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-word-abbreviation/submissions/1834026154/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-01


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ptr_w = ptr_a = 0

        while ptr_a < len(abbr) and ptr_w < len(word):
            if abbr[ptr_a].isdigit():
                if abbr[ptr_a] == '0':
                    return False
            
                count = 0
                while ptr_a < len(abbr) and abbr[ptr_a].isdigit():
                    count = count * 10 + int(abbr[ptr_a])
                    ptr_a += 1
                ptr_w += count
            else:    
                if abbr[ptr_a] != word[ptr_w]:
                    return False
                ptr_a += 1
                ptr_w += 1
        return ptr_a == len(abbr) and ptr_w == len(word)
                


