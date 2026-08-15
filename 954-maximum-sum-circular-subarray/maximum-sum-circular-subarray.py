class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minend=nums[0]
        maxend=nums[0]
        maxsum=nums[0]
        minsum=nums[0]
        res=nums[0]
        s=nums[0]
        for i in range(1,len(nums)):
            maxend=max(nums[i],maxend+nums[i])
            minend=min(nums[i],minend+nums[i])
            maxsum=max(maxsum,maxend)
            minsum=min(minsum,minend)
            s+=nums[i]
        if maxsum<0:
            return maxsum    
        c=s-minsum
        return max(c,maxsum) 
        