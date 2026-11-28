class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        s = set()
        m = defaultdict(list)

        for e in edges:
            m[e[0]].append(e[1])
            m[e[1]].append(e[0])
        
        def dfs(node):
            if node in s:
                return
            
            s.add(node)
            for neibor in m[node]:
                dfs(neibor)
        res = 0
        for i in range(n):
            if i not in s:
                dfs(i)
                res += 1
        
        return res

