class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            pairSum = numbers[lp] + numbers[rp]

            if pairSum == target:
                return [lp + 1, rp + 1]
            elif pairSum > target:
                rp -= 1
            else:
                lp += 1