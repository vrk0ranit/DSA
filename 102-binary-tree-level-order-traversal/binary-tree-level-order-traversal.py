# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def fun(node,level):
            if node is None:
                return 
            if len(res)==level:
                res.append([])
            res[level].append(node.val)  
            fun(node.left,level+1)         
            fun(node.right,level+1)    
        fun(root,0)
        return res         
