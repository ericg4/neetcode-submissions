class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        [1,1,2]
        """

        res = []

        nums.sort()
        n = len(nums)

        def backtrack(idx, subset):
            if idx >= n:
                res.append(subset.copy())
                return
            
            subset.append(nums[idx])
            # use it
            idx += 1
            backtrack(idx, subset)

            # or move on
            while (idx < n and nums[idx] == nums[idx - 1]):
                idx += 1
            
            subset.pop()
            
            backtrack(idx, subset)
        
        backtrack(0, [])
            
        return res

            
