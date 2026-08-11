class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], 
            '9': ['w', 'x', 'y', 'z']
        }

        n = len(digits)
        res = []

        def backtrack(idx, substring):
            if idx >= n:
                res.append(substring)
                return
            
            # go through all letters that the digit could map to
            letters = digitMap[digits[idx]]
            for c in letters:
                backtrack(idx + 1, substring + c)
            
        backtrack(0, "")
        if res[0] != "":
            return res
        else:
            return []