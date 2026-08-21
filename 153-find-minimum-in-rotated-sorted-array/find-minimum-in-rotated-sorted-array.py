class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        res=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>nums[n-1]:
                low=mid+1
            else:
                res=mid
                high=mid-1
        return nums[res]            


        