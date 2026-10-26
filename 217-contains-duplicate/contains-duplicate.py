class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        f={}
        for num in nums:
            if num in f:
                f[num]+=1
            else:
                f[num]=1
        for key in f:
            if f[key]>=2:
                return True
        return False                        
        