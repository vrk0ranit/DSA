class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=""
        for char in s:
            if char.isalnum():
                word+=char.lower()
        # if word==word[::-1]:
        #     return True
        # else:
        #     return False   
        i=0
        j=len(word)-1
        while i<j:
            if word[i]!=word[j]:
                return False
            i+=1
            j-=1    
        return True         