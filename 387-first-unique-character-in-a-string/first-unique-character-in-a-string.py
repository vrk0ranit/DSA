class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for ch in s:
            if ch in f:
                f[ch]+=1
            else:
                f[ch]=1
        for i in range(len(s)):
            if f[s[i]]==1:
                return i
        return -1                   

        