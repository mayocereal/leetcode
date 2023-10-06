# 242. Valid Anagram (Easy)

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        hashmapS, hashmapT = {}, {}

        for index in range(len(s)):
            hashmapS[s[index]] = 1 + hashmapS.get(s[index], 0)
            hashmapT[t[index]] = 1 + hashmapT.get(t[index], 0)
        
        return hashmapS == hashmapT