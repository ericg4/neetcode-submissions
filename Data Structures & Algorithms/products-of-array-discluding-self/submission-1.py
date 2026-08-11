class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1 ,2 ,4,6]
        [1 ,1 ,2,8] prefix
        [48,24,6,1] suffix
        """

        output = [1] * len(nums)

        prefix = nums[0]

        for i in range(1, len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
        
        suffix = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output