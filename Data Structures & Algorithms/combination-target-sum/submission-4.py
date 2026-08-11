class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        2,5,6,9

        """
        result = []
        digs = []

        def dfs(i, curSum):
            if curSum > target or i == len(nums):
                return
            elif curSum == target:
                result.append(digs.copy())
                return
            
            digs.append(nums[i])
            dfs(i, curSum + nums[i])
            digs.pop()
            dfs(i+1, curSum)
        
        dfs(0, 0)

        return result
            
