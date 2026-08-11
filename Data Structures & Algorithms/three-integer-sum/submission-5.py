class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -4,-1,-1,0,1,2
        """
        nums.sort()

        res = []

        i = 0
        prev = float("-inf")
        while i < len(nums) - 1:
            if nums[i] > 0:
                return res
            
            l = i + 1
            r = len(nums) - 1

            complement = -nums[i]

            while l < r:
                twoSum = nums[l] + nums[r]

                if twoSum > complement:
                    r -= 1
                elif twoSum < complement:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    prev = nums[r]
                    while l < r and nums[r] == prev:
                        r -= 1
            prev = nums[i]
            i += 1
            while i < len(nums) and nums[i] == prev:
                i += 1
            
        return res