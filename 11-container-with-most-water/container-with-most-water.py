class Solution:
    def maxArea(self, height: list[int]) -> int:
        i=0
        j=len(height)-1
        max_water=0
        while i<j:
            w=j-i
            h=min(height[i],height[j])
            max_water=max(max_water,h*w)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_water            
        