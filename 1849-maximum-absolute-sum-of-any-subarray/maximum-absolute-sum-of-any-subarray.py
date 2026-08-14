class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxend=nums[0]
        minend=nums[0]
        res=abs(nums[0])
        for i in range(1,len(nums)):
            minend=min(nums[i],minend+nums[i])
            maxend=max(nums[i],maxend+nums[i])
            res=max(res,abs(maxend),abs(minend))
        return res    