class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m = defaultdict(list)
        s = set()

        for u,v in edges:
            m[u].append(v)
            m[v].append(u)
        
        cycles = set()
        self.c = -1

        def dfs(node, par):
            if node in s:
                self.c = node
                return node
            
            s.add(node)
            
            for n in m[node]:
                if n == par:
                    continue
                r = dfs(n, node)
                if r:
                    if self.c != -1:
                        cycles.add(node)
                    if node == self.c:
                        self.c = -1
                    return r
        
        joint = dfs(2, -1)
        print(joint, cycles)
        
        for i in range(len(edges)-1,-1,-1):
            u,v = edges[i]
            if u in cycles and v in cycles:
                return [u,v]
        
        return []






