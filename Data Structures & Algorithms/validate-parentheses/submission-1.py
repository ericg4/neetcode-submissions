class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        correlations = {"}": "{", "]": "[", ")": "("}

        for i in range(len(s)):
            if s[i] in set(["{", "[", "("]):
                stack.append(s[i])
            else:
                if stack and stack[-1] == correlations[s[i]]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0