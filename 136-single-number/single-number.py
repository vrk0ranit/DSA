class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        f={}
        for num in nums:
            if num in f:
                f[num]+=1
            else:
                f[num]=1
        for key in f:
            if f[key]==1:
                return key            
        