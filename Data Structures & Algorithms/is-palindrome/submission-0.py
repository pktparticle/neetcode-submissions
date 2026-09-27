class Solution:
    def isAlphaNumeric(self, char):
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
            return True
        return False

    def toLower(self, char):
        if 'A' <= char <= 'Z':
            return chr(ord(char)+32)
        return char

    def isPalindrome(self, s: str) -> bool:
        clean = []
        for i in range(len(s)):
            char = s[i]
            if self.isAlphaNumeric(char):
                clean.append(self.toLower(char))
        cleanLength = len(clean)
        left, right = 0, cleanLength-1
        while left < right:
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1
        return True