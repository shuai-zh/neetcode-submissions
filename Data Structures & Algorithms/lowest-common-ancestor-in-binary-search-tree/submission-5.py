# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        res = None
        
        def dfs(root):
            if not root:
                return None
            
            left, right = None, None
            if p.val < root.val or q.val < root.val:
                left = dfs(root.left)
            if p.val > root.val or q.val > root.val:
                right = dfs(root.right)

            if left and right and left.val == p.val and right.val == q.val:
                
                return root
            if left and right and left.val == q.val and right.val == p.val:
                
                return root
            if left and left.val == p.val and root.val == q.val:
                
                return root
            if left and left.val == q.val and root.val == p.val:
                
                return root
            if right and right.val == p.val and root.val == q.val:
                
                return root
            if left and right and right.val == q.val and root.val == p.val:
                return root
            
            
            node = left if left else right
            if root.val == p.val or root.val == q.val:
                node = root
            return node
        return dfs(root)

        
            

            

        