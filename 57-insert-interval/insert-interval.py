class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        start1=newInterval[0]
        end1=newInterval[1]
        res=[]
        for i in range(len(intervals)):
            start2=intervals[i][0]
            end2=intervals[i][1]
            if end2<start1:
                res.append([start2,end2])
            elif end1<start2:
                res.append([start1,end1])
                start1=start2
                end1=end2
            else:
                start1=min(start1,start2) 
                end1=max(end1,end2)       
        res.append([start1,end1])     
        return res   

        