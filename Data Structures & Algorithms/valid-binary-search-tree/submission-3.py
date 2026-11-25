# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
         

        def dfs(root, left,right):
            if not root:
                return True
            
            l = dfs(root.left, root.val,right)
            r = dfs(root.right, left, root.val)

            return root.val < left and root.val > right and l and r
        
        return dfs(root, float('inf'), -float('inf'))
        
