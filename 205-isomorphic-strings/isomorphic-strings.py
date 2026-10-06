class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        f={}
        c={}
        for a,b in zip(s,t):
            if a in f and f[a]!=b:
                return False
            if b in c and c[b]!=a:
                return False
            f[a]=b
            c[b]=a 
        return True           