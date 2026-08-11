class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        2,5,6,9

        """
        
        options = []
        results = []
        nums.sort()

        def backtrack(i, total):
            if total == target:
                results.append(options.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                options.append(nums[j])
                backtrack(j, total + nums[j])
                options.pop()
        
        backtrack(0, 0)
        return results
            