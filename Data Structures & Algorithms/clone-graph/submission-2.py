"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}

        def dfs(node):
            if not node:
                return None
            
            if node.val in node_map:
                new_node = node_map[node.val]
            else:
                new_node = Node(node.val)
            
            node_map[node.val] = new_node
            new_neighbors = []
            for n in node.neighbors:
                if n.val in node_map:
                    new_neighbors.append(node_map[n.val])
                else:
                    new_neighbors.append(dfs(n))
                
            new_node.neighbors = new_neighbors
            return new_node
        return dfs(node)
        

