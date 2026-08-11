class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        [5]
        """

        stack = []

        for item in tokens:
            if item in set(["+","*","/","-"]):
                second = stack.pop()
                first = stack.pop()

                if item == "+":
                    result = first + second
                elif item == "*":
                    result = first * second
                elif item == "/":
                    result = int(float(first) / second)
                elif item == "-":
                    result = first - second

                stack.append(result)
            else:
                stack.append(int(item))
        
        return stack[0]