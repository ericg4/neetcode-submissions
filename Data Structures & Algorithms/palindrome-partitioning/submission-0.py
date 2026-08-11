class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """

        """

        res = []

        def backtrack(i, j, substring):
            if j >= len(s):
                res.append(substring.copy())
                return
            
            # more substring only if there's room for more substring
            if (j < len(s) - 1):
                backtrack(i, j+1, substring)

            # or move on to next substring
            # check if palindrome:
            l = i
            r = j
            while (l < j):
                # if not palindrome return
                if s[l] != s[r]:
                    return
                l += 1
                r -= 1
            substring.append(s[i:j + 1])
            backtrack(j+1, j+1, substring)
            substring.pop()
        
        backtrack(0, 0, [])
        return res