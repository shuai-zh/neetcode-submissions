class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = defaultdict(list)
        for p in prerequisites:
            m[p[0]].append(p[1])
        visited = [0] * numCourses
        

        def dfs(c):
            if visited[c] == 1:
                return False
            if visited[c] == 2:
                return True
            
            pre = m[c]
            visited[c] = 1

            for p in pre:
                if not dfs(p):
                    return False
                    
            visited[c] = 2
            return True
        for i in range(numCourses):
            
            if visited[i] == 0 and not dfs(i):
                return False
        return True

