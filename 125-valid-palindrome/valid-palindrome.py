class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=""
        for char in s:
            if char.isalnum():
                word+=char.lower()
        if word==word[::-1]:
            return True
        else:
            return False    