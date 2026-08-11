class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isSpeedValid(speed):
            totalHours = 0
            for num in piles:
                totalHours += num // speed
                if num % speed:
                    totalHours += 1
            if totalHours > h:
                return False
            return True
        
        low = 1
        high = max(piles)

        minSpeed = high

        while low <= high:
            mid = low + ((high - low) // 2)

            isValid = isSpeedValid(mid)

            if isValid:
                high = mid - 1
                minSpeed = mid
            else:
                low = mid + 1
        
        return minSpeed
            
        

