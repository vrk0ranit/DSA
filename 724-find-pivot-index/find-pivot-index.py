class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
        if sum-nums[0]==0:
            return 0  
        for i in range(1,len(nums)):
            left+=nums[i-1]
            right=sum-left-nums[i]
            if left==right:
                return i
        return -1