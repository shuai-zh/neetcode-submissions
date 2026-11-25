# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0

        def dfs(root, pre):
            if not root:
                return 
            
            if root.val >= pre:
                self.res += 1
            
            dfs(root.left, max(root.val, pre))
            dfs(root.right, max(root.val, pre))
        
        dfs(root, root.val)
        return self.res