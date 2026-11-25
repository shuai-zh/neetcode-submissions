# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_map = {}

        for i in range(len(inorder)):
            val_map[inorder[i]] = i
        
        self.index_preoder = 0
        
        def dfs(l,r):
            if l > r:
                return None
        
            root = preorder[self.index_preoder]
            
            index = val_map[root]


            root_node = TreeNode(root)
            
            self.index_preoder += 1

            root_node.left = dfs(l,index-1)
            root_node.right = dfs(index+1,r)
            return root_node
        return dfs(0,len(inorder)-1)
