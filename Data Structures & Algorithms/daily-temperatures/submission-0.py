class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [30,38,30,36,35,40,28]
        [(30,0), ]
        """
        result = [0 for _ in range(len(temperatures))]

        stack = [] # (idx, temp)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                diff = idx - stack[-1][0]

                result[stack[-1][0]] = diff
                stack.pop()
            
            stack.append((idx, temp))
        
        return result