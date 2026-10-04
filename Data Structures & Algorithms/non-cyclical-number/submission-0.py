class Solution:
    def sumOfSqauresOfDigits(self, n: int) -> int:
        digitSquareSum = 0
        while n > 0:
            digit = n%10
            digitSquareSum += digit * digit
            n //= 10
        return digitSquareSum

    def isHappy(self, n: int) -> bool:
        seen = set()
        digitSquareSum = self.sumOfSqauresOfDigits(n)
        while digitSquareSum != 1 and digitSquareSum not in seen:
            seen.add(digitSquareSum)
            digitSquareSum = self.sumOfSqauresOfDigits(digitSquareSum)
        if digitSquareSum in seen:
            return False
        elif digitSquareSum == 1:
            return True