class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        2,5,6,9

        """
        
        options = []
        results = []

        def backtrack(i, tempSum):
            if tempSum > target or i >= len(nums):
                return
            elif tempSum == target:
                results.append(options.copy())
                return
                        
            # append number
            options.append(nums[i])
            backtrack(i, tempSum + nums[i])

            options.pop()
            
            # try move on
            backtrack(i + 1, tempSum)
        
        backtrack(0, 0)
        return results
            