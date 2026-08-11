class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for word in strs:
            letterCounts = [0] * 26
            for i in range(len(word)):
                letterPos = ord(word[i]) - ord('a')
                letterCounts[letterPos] += 1
            
            hashableCounts = tuple(letterCounts)
            
            if hashableCounts in anagramMap:
                anagramMap[hashableCounts].append(word)
            else:
                anagramMap[hashableCounts] = [word]

        result = []
        
        for key, wordList in anagramMap.items():
            result.append(wordList)
        
        return result