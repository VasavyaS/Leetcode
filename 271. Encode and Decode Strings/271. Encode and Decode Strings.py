#
# Problem: 271. Encode and Decode Strings
# Difficulty: Medium
# Link: https://leetcode.com/problems/encode-and-decode-strings/description/
# Language: python3
# Date: 2026-01-11


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for w in strs:
            encoded += str(len(w))+'#'+w
        return encoded

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        words = []
        i = 0
        while i < len(s):
            p = s.find('#', i)
            length = int(s[i:p])
            words.append(s[p+1:p+1+length])
            i = p+1+length
        return words
# O(n) O(k)
# We don't count the output as part of the space complexity, but for each word, we are using some space for the length and delimiter.

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
