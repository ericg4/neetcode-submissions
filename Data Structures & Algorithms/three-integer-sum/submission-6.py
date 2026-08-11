class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -4,-1,-1,0,1,2
        """
        nums.sort()

        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[l] + nums[r] + a

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    prev = nums[r]
                    while l < r and nums[r] == prev:
                        r -= 1
            
        return res