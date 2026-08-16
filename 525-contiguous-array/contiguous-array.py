class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        f={}
        res=0
        z=0
        o=0
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
            else:
                o+=1
            diff=z-o 
            if diff==0:
                res=max(res,i+1)
                continue
            if diff in f:
                res=max(res,i-f[diff])
            else:
                f[diff]=i
        return res                       
        