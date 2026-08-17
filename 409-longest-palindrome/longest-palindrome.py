class Solution:
    def longestPalindrome(self, s: str) -> int:
        f={}
        for ch in s:
            if ch in f:
                f[ch]+=1
            else:
                f[ch]=1
        l=0
        odd=False
        for c in f.values():
            l+=(c//2)*2     
            if c%2==1:
                odd=True
        if odd:
            l+=1  
        return l             