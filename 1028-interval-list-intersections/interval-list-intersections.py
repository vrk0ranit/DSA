class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        res=[]
        while i<len(firstList) and j<len(secondList):
            start1=firstList[i][0]
            end1=firstList[i][1]
            start2=secondList[j][0]
            end2=secondList[j][1]
            start=max(start1,start2)
            end=min(end1,end2)
            if end>=start:
                res.append([start,end])
            if end1<end2:
                i+=1
            else:
                j+=1
        return res                

        