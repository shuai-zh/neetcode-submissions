"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}

        

        def copy(node):
            if not node:
                return None
            if node in node_map:
                return node_map[node]
            copy_next = None
            copy_random = None
            new_node = Node(node.val)
            node_map[node] = new_node

            copy_next = copy(node.next)
            copy_random = copy(node.random)
            new_node.next = copy_next
            new_node.random = copy_random
            
            
            return new_node
        
        
        return copy(head)


            