class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []
        n = len(temperatures)
        for i in range(n-1, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0]<=temp:
                stack.pop()
            if stack:
                result.append(stack[-1][1]-i)
            else:
                result.append(0)
            stack.append((temp,i))
        return result[::-1]        