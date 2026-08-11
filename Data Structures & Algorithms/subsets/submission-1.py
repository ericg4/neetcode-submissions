class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """

        """

        result = []

        def dfs(i, cur):
            if i == len(nums):
                result.append(cur.copy())
                return
            
            # Skip digit
            dfs(i + 1, cur)
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            
        dfs(0, [])
        return result

