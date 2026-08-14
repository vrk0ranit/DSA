class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodel=arr[0]
        onedel=float('-inf')
        res=arr[0]
        for i in range(1,len(arr)):
            old_del=nodel
            nodel=max(arr[i],nodel+arr[i])
            onedel=max(onedel+arr[i],old_del)
            res=max(res,onedel,nodel)
        return res    

        