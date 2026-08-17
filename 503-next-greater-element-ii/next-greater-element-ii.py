class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums)
        for i in range(2*len(nums)-1,-1,-1):
            idx=i%len(nums)
            while stack and nums[idx]>=stack[-1]:
                stack.pop()
            if stack:
                res[idx]=stack[-1]
            stack.append(nums[idx])    
        return res    

        