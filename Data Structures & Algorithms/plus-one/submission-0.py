class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(1+int(''.join(str(d) for d in digits))))

        