class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for c in s:
            if not stack:
                stack.append([c,1])
                continue
            if stack[-1][0]!=c:
                stack.append([c,1])
                continue
            if stack[-1][1]<k-1:
                p=stack.pop()
                stack.append([p[0],p[1]+1])
                continue
            stack.pop()
        res=""
        while stack:
            p=stack.pop()
            while p[1]>0:
                res+=p[0]
                p[1]-=1
        return res[::-1]                    
        
        