class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        i=0
        for j in range(1,len(nums)):
            if nums[i]==nums[j]:
                return True
                break
            i+=1
        return False        
        