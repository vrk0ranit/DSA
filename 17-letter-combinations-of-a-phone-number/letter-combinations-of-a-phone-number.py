class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        f={}
        f["2"]="abc"
        f["3"]="def"
        f["4"]="ghi"
        f["5"]="jkl"
        f["6"]="mno"
        f["7"]="pqrs"
        f["8"]="tuv"
        f["9"]="wxyz"
        n=len(digits)
        idx=0
        diary=[]
        res=[]
        def fun(s,n,idx,diary,res):
            if idx==n:
                res.append("".join(diary))
                return
            choice=f[s[idx]]
            for j in range(0,len(choice)):
                diary.append(choice[j])
                fun(s,n,idx+1,diary,res)
                diary.pop()   
            return     
        fun(digits,n,idx,diary,res)
        return res
        