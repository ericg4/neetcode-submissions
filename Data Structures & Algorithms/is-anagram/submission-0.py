class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charSet = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in charSet:
                charSet[s[i]] += 1
            else:
                charSet[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in charSet:
                if charSet[t[i]] >= 1:
                    charSet[t[i]] -= 1
                else:
                    return False
            else:
                return False
        
        for key, val in charSet.items():
            if val != 0:
                return False
        
        return True
