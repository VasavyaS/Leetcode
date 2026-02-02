#
# Problem: 824. Goat Latin
# Difficulty: Easy
# Link: https://leetcode.com/problems/goat-latin/submissions/1904901489/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-02


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')

        for i,w in enumerate(words):
            if w[0] in 'aeiou' or w[0] in 'AEIOU':
                w = w + "ma"
            else:
                w = w[1:len(w)] + w[0] + "ma"
            w = w + 'a'*(i +1)
            words[i] = w
        return " ".join(words)

