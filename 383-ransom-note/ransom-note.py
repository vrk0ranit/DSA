class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f={}
        for ch in magazine:
            if ch in f:
                f[ch]+=1
            else:
                f[ch]=1
        for ch in ransomNote:
            if ch not in f or f[ch]==0:
                return False  
            f[ch]-=1
        return True                  
        