class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isValidChar(char):
            return ((ord('a') <= ord(char) <= ord('z')) or
                (ord('A') <= ord(char) <= ord('Z')) or
                (ord('0') <= ord(char) <= ord('9')))
        
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            while not isValidChar(s[lp]) and lp < rp:
                lp += 1
            while not isValidChar(s[rp]) and lp < rp:
                rp -= 1
            
            print(s[lp], s[rp])
            
            if s[lp].lower() != s[rp].lower():
                return False
            
            lp += 1
            rp -= 1

        return True
