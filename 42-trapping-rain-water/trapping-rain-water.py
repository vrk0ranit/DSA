class Solution:
    def trap(self, height: list[int]) -> int:
        n=len(height)
        water=0
        l=0
        r=n-1
        l_m=0
        r_m=0
        while l<r:
            if height[l]<=height[r]:
                if height[l]>l_m:
                    l_m=height[l]
                else:
                    water+=l_m-height[l]
                    l+=1
            else:
                if height[r]>r_m:
                    r_m=height[r]
                else:
                    water+=r_m-height[r]
                    r-=1
        return water                            

         