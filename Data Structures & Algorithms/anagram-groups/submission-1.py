class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for gram in strs:
            count = [0] * 26

            for let in gram:
                idx = ord(let) - ord('a')
                count[idx] += 1
            
            count = tuple(count)
            if count in anagram_map:
                anagram_map[count].append(gram)
            else:
                anagram_map[count] = [gram]
        
        return [value for key, value in anagram_map.items()]