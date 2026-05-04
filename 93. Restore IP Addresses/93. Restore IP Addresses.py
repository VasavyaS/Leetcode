#
# Problem: 93. Restore IP Addresses
# Difficulty: Medium
# Link: https://leetcode.com/problems/restore-ip-addresses/description/?envType=company&envId=palo-alto-networks&favoriteSlug=palo-alto-networks-more-than-six-months
# Language: python3
# Date: 2026-05-04


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        if len(s) > 12:
            return []
        
        def backtrack(i, dots, curIP):
            if i == len(s) and dots == 4:
                res.append(curIP[:-1]) #append everyhting except the 4th dot
                return
            if dots > 4:
                return
            
            for j in range(i, min(len(s), i+3)):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != '0'): #the int < 256 and its single char or beginning is not 0
                    backtrack(j+1, dots+1, curIP+s[i:j+1]+'.')
        backtrack(0,0,"")
        return res
