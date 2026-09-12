class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        idx=0
        n=len(candidates)
        diary=[]
        sum=0
        res=[]
        def fun(a,n,idx,diary,sum,res,target):
            if idx==n:
                if sum==target:
                    res.append(diary.copy())
                return
            fun(a,n,idx+1,diary,sum,res,target)
            if a[idx]+sum<=target:
                diary.append(a[idx])
                sum=sum+a[idx]       
                fun(a,n,idx,diary,sum,res,target)  
                diary.pop()
                sum=sum-a[idx]
            return
        fun(candidates,n,idx,diary,sum,res,target)    
        return res

