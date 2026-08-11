class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i in range(len(nums)):
            val = nums[i]

            if val in complements:
                return [complements[val], i]
            
            complements[target-val] = i
        