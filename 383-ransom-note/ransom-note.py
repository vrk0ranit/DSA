class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        f={}
        for ch in magazine:
            f[ch]=f.get(ch,0)+1
        for ch in ransomNote:
            if ch not in f or f[ch]==0:
                return False
            f[ch]-=1
        return True            