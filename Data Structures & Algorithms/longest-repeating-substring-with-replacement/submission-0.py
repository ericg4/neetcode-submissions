class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def findMaxFreq(charSet):
            maxFreq = 0
            importantKey = None
            for key, val in charSet.items():
                if val > maxFreq:
                    maxFreq = val
                    importantKey = key
            return importantKey, maxFreq

        l = 0
        r = 0

        maxLen = r - l + 1

        charSet = {}

        while r < len(s):
            charSet[s[r]] = charSet.get(s[r], 0) + 1
            key, maxFreq = findMaxFreq(charSet)
            print(l, r)
            print(key, maxFreq)
            windowLen = r - l + 1
            if windowLen - maxFreq <= k:
                if windowLen > maxLen:
                    maxLen = windowLen
                print("maxLen:", maxLen)
            while windowLen - maxFreq > k:
                charSet[s[l]] -= 1
                l += 1
                windowLen = r - l + 1
                _, maxFreq = findMaxFreq(charSet)
            
            r += 1
        
        return maxLen
