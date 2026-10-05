class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxprofit=float("-inf")
        minPrice=float("inf")
        if len(prices)<=1:
            return 0
        i=0
        for j in range(1,len(prices)):
            minPrice=min(minPrice,min(prices[i],prices[j]))
            maxprofit=max(maxprofit,prices[j]-minPrice)
            i+=1
        return maxprofit    
        