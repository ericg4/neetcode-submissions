class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        1,2,3,4,5,6
        l         r
        2,3,4,5,6,1
        5,6,1,2,3,4
        6,1,2,3,4,5
        """
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res