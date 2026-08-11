class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []

        for word in strs:
            arr.append(str(len(word)) + "#")
            arr.append(word)
        
        return "".join(arr)

    def decode(self, s: str) -> List[str]:
        arr = []

        num = 0

        i = 0

        while i < len(s):
            wordLen = 0
            while s[i] != "#":
                wordLen *= 10
                wordLen += int(s[i])
                i += 1
            
            word = []
            i += 1

            while wordLen > 0:
                word.append(s[i])
                i += 1
                wordLen -= 1
            
            arr.append("".join(word))
        
        return arr
            
