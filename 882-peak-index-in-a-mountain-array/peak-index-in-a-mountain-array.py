class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low=0
        high=len(arr)-1
        while low<=high:
            guess=(low+high)//2
            if arr[guess]>arr[guess+1] and arr[guess]>arr[guess-1]:
                return guess
            elif arr[guess]<arr[guess+1] and arr[guess]>arr[guess-1]:
                low=guess+1
            elif arr[guess]>arr[guess+1] and arr[guess]<arr[guess-1]:
                high=guess-1
            elif arr[guess]==arr[len(arr)-1]:
                high=guess-1
            else:
                low=guess+1  
        return -1                  
        
        