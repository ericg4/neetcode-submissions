class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        charSet = defaultdict()
        charSet[s[0]] = 1

        l = 0
        r = 1

        maxLength = r - l

        while r < len(s):
            print(l, r)
            if charSet.get(s[r], 0) == 0:
                charSet[s[r]] = charSet.get(s[r], 0) + 1
                r += 1
                maxLength = max(maxLength, r - l)
            else:
                charSet[s[r]] += 1
                while charSet[s[r]] > 1:
                    charSet[s[l]] -= 1
                    l += 1
                r += 1
                
        return maxLength