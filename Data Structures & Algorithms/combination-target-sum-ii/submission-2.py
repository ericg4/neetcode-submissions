class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        options = []
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(options.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            options.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            options.pop()

            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            
            backtrack(i, total)
        
        backtrack(0, 0)
        return res
            
                    
