class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t in '+-*/':
                num1=stack.pop()
                num2=stack.pop()
                if t == '+':
                    res = num2+num1
                elif t == '-':
                    res = num2-num1
                elif t == '*':
                    res = num2*num1
                else:
                    res = int(float(num2)/num1)
                stack.append(res)
            else:
                stack.append(int(t))
            # print(stack)
        return stack[-1]


        