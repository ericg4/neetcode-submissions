class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1 ,2 ,4,6]
        [1 ,1 ,2,8] prefix
        [48,24,6,1] suffix
        """

        resultArr = [1 for _ in range(len(nums))]

        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            resultArr[i] *= prefix
        
        suffix = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1]
            resultArr[i] *= suffix
        
        return resultArr