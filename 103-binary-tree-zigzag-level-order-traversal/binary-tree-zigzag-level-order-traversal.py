# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque([root])
        res=[]
        left_to_right=True
        while q:
            level=[]
            for _ in range(len(q)):
                Node=q.popleft()
                level.append(Node.val)
                if Node.left:
                    q.append(Node.left) 
                if Node.right:
                    q.append(Node.right)   
            if not left_to_right:
                level.reverse()    
            res.append(level)     
            left_to_right= not left_to_right
        return res 
        