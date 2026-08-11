class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Counts = {}

        for char in s1:
            s1Counts[char] = s1Counts.get(char, 0) + 1

        print(s1Counts)
        
        for i in range(len(s1)):
            s1Counts[s2[i]] = s1Counts.get(s2[i], 0) - 1
            if s1Counts[s2[i]] == 0:
                del s1Counts[s2[i]]
        
        print(s1Counts)

        l = 0
        r = len(s1) - 1

        while r < len(s2) - 1:
            if not s1Counts:
                return True
            
            print(s1Counts)
            
            s1Counts[s2[l]] = s1Counts.get(s2[l], 0) + 1
            if s1Counts[s2[l]] == 0:
                del s1Counts[s2[l]]
            
            l += 1
            r += 1

            s1Counts[s2[r]] = s1Counts.get(s2[r], 0) - 1
            if s1Counts[s2[r]] == 0:
                del s1Counts[s2[r]]
            
        if not s1Counts:
            return True
        return False

        
