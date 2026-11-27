class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        s = set()
        m = defaultdict(list)

        for e in edges:
            m[e[0]].append(e[1])
            m[e[1]].append(e[0])

        def dfs(node, parent):
            
            if node in s:
                return False
            
            s.add(node)
            
            for i in m[node]:
                if i != parent and not dfs(i, node):
                    return False
            return True
        
        return dfs(0, -1) and len(s) == n

