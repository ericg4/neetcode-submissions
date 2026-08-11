class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = [0] * 26
        counts2 = [0] * 26

        if len(s1) > len(s2):
            return False

        def getIdx(char):
            return ord(char) - ord('a')
        
        for i in range(len(s1)):
            counts1[getIdx(s1[i])] += 1
            counts2[getIdx(s2[i])] += 1

        matches = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = getIdx(s2[r])
            counts2[idx] += 1
            if counts1[idx] == counts2[idx]:
                matches += 1
            elif counts1[idx] + 1 == counts2[idx]:
                matches -= 1
            
            idx = getIdx(s2[l])
            counts2[idx] -= 1
            if counts1[idx] == counts2[idx]:
                matches += 1
            elif counts1[idx] - 1 == counts2[idx]:
                matches -= 1
            l += 1
        
        return matches == 26
