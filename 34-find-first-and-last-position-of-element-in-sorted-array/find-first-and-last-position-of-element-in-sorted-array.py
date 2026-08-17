class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                first=mid
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        second=-1
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                second=mid
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1   
        return [first,second]                   