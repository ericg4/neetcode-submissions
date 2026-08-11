class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        sCnt = [0] * 300
        tCnt = [0] * 300

        for i in range(len(t)):
            sCnt[ord(s[i]) - ord('a')] += 1
            tCnt[ord(t[i]) - ord('a')] += 1
        
        neededMatches = 0
        matches = 0

        minLen = len(s)
        bestStr = s

        for i in range(300):
            if tCnt[i] > 0:
                neededMatches += 1
                if sCnt[i] >= tCnt[i]:
                    matches += 1


        found = False   
        l = 0
        for r in range(len(t), len(s) + 1):
            print(s[l:r], matches)
            while matches == neededMatches and l < r:
                if r - l <= minLen:
                    minLen = r - l
                    bestStr = s[l:r]
                    print("new best:", bestStr)
                    found = True
                
                lIdx = ord(s[l]) - ord('a')
                sCnt[lIdx] -= 1
                if tCnt[lIdx] > 0 and sCnt[lIdx] == tCnt[lIdx] - 1:
                    matches -= 1
                l += 1
            print(s[l:r], matches)

            if r < len(s):
                rIdx = ord(s[r]) - ord('a')
                sCnt[rIdx] += 1
                print(s[r])
                print(sCnt[rIdx])
                print(tCnt[rIdx])
                if tCnt[rIdx] > 0 and sCnt[rIdx] == tCnt[rIdx]:
                    matches += 1
        
        return bestStr if found else ""

            
            
            