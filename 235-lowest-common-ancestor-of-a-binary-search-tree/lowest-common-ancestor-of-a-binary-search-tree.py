# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=None
        def fun(root,p,q):
            nonlocal ans
            if root is None:
                return
            if root==p or root==q:
                ans=root
                return
            if root.val<p.val:
                fun(root.right,p,q)
            elif root.val>q.val:
                fun(root.left,p,q)
            else:
                ans=root
                return                
        if p.val<q.val:
            fun(root,p,q)
        else:
            fun(root,q,p)   
        return ans     