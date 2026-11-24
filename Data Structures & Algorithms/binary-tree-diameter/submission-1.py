# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        
        def dfs(root):
            if not root or (not root.left and not root.right):
                return 0
            left = 0
            right = 0
            if root.left:
                left = dfs(root.left) + 1
            if root.right:
                right = dfs(root.right) + 1
            
            
            nonlocal res
            res = max(res, left+right)
            return max(left,right)
        
        dfs(root)
        return res


        