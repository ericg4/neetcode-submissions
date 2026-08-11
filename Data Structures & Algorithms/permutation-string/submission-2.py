class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Counts = [0] * 26
        s2Counts = [0] * 26

        for i in range(len(s1)):
            s1Counts[ord(s1[i]) - ord('a')] += 1
            s2Counts[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Counts[i] == s2Counts[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            rIndex = ord(s2[r]) - ord('a')
            s2Counts[rIndex] += 1
            if s2Counts[rIndex] == s1Counts[rIndex]:
                matches += 1
            elif s2Counts[rIndex] == s1Counts[rIndex] + 1:
                matches -= 1

            lIndex = ord(s2[l]) - ord('a')
            s2Counts[lIndex] -= 1
            if s2Counts[lIndex] == s1Counts[lIndex]:
                matches += 1
            elif s2Counts[lIndex] == s1Counts[lIndex] - 1:
                matches -= 1
            l += 1
        
        return matches == 26
            

