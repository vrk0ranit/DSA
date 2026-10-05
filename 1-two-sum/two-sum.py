class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr=[(num,i) for i,num in enumerate(nums)]
        arr.sort()
        i=0
        j=len(nums)-1
        while i<j:
            s=arr[i][0]+arr[j][0]
            if s==target:
                return [arr[i][1],arr[j][1]]
                break
            elif s>target:
                j-=1
            else:
                i+=1   

        