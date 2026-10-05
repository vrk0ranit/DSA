class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=j=0
        res=[]
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i<m:
            res.append(nums1[i])
            i+=1
        while j<n:
            res.append(nums2[j])
            j+=1            
        for i in range(m+n):
            nums1[i]=res[i]          
        