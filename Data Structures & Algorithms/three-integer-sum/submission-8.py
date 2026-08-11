class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -1, 0, 1, 2, -1, -4
        brute force: 
        all sets of 3 unique numbers that add to 0 -- n^3

        2-sum approach: 
        map of all numbers to their locations, look for complementary number -- show the 2 indices

        3-sum approach: 
        don't need indices
        -1 -> need +1 sum of 2 numbers (or sort, two-pointers)

        0. edge cases: 
        <3 numbers -- return empty list
        no negatives (first sorted is positive) -- return empty list
        1. sort
        2. choose first number as root
        3. take complement number as goal
        4. start at next number with l pointer, end number w r pointer
        5. work your way in until the middle (adding matching sets as you go)

        """
        result = []

        if (len(nums) < 3):
            return result
        
        sorted_nums = sorted(nums)

        if (sorted_nums[0] > 0):
            return result

        for i in range(len(sorted_nums)):
            if (i > 0 and sorted_nums[i - 1] == sorted_nums[i]):
                continue
            anchor_num = sorted_nums[i]
            complement_num = -anchor_num

            if (anchor_num > 0):
                break

            l_ptr = i + 1
            r_ptr = len(sorted_nums) - 1

            while (l_ptr < r_ptr):
                l_num = sorted_nums[l_ptr]
                r_num = sorted_nums[r_ptr]

                if (l_num + r_num > complement_num):
                    while (l_ptr < r_ptr - 1 and sorted_nums[r_ptr - 1] == sorted_nums[r_ptr]):
                        r_ptr -= 1
                    r_ptr -= 1
                elif (l_num + r_num < complement_num):
                    while (l_ptr + 1 < r_ptr and sorted_nums[l_ptr + 1] == sorted_nums[l_ptr]):
                        l_ptr += 1
                    l_ptr += 1
                else:
                    result.append([anchor_num, l_num, r_num])
                    while (l_ptr + 1 < r_ptr and sorted_nums[l_ptr + 1] == sorted_nums[l_ptr]):
                        l_ptr += 1
                    l_ptr += 1
                    while (l_ptr < r_ptr - 1 and sorted_nums[r_ptr - 1] == sorted_nums[r_ptr]):
                        r_ptr -= 1
                    r_ptr -= 1


        return result
