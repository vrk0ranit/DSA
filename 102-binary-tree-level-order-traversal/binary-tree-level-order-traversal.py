# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque([root])
        res=[]
        while q:
            level=[]
            for _ in range(len(q)):
                Node=q.popleft()
                level.append(Node.val)
                if Node.left:
                    q.append(Node.left) 
                if Node.right:
                    q.append(Node.right)   
            res.append(level)     
        return res         
        