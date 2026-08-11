class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0

        maxLen = 1

        charSet = {}
        maxFreq = 0

        while r < len(s):
            charSet[s[r]] = charSet.get(s[r], 0) + 1

            if charSet[s[r]] > maxFreq:
                maxFreq = charSet[s[r]]
            
            if r - l + 1 - maxFreq <= k:
                maxLen = max(r - l + 1, maxLen)
            
            while r - l + 1 - maxFreq > k:
                charSet[s[l]] -= 1
                l += 1
            r += 1
        
        return maxLen