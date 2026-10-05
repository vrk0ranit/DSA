class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s=sum(nums)
        n=len(nums)
        c=(n*(n+1))//2
        x=c-s
        return x