# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=None
        def fun(node,p,q):
            nonlocal ans
            if node is None:
                return 0
            left=fun(node.left,p,q)    
            right=fun(node.right,p,q)    
            slf=0
            if node==p or node==q:
                slf=1
            total=left+right+slf
            if total==2 and ans is None:
                ans=node
            return total
        fun(root,p,q)     
        return ans       