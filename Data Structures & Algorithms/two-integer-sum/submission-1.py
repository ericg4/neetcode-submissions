class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            num = nums[i]
            num_map[num] = i
        
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in num_map:
                if i == num_map[complement]:
                    continue
                
                return sorted([i, num_map[complement]])
                