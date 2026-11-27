class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = defaultdict(list)
        indegree = [0] * numCourses

        for p in prerequisites:
            m[p[1]].append(p[0])
            indegree[p[0]] += 1
        
       
        starting_indegree = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                starting_indegree.append(i)
        
        res = []
        
        while starting_indegree:
            length = len(starting_indegree)
            while length>0:
                cur = starting_indegree.pop()
                res.append(cur)
                for out in m[cur]:
                    indegree[out] -= 1
                    if indegree[out] == 0:
                        
                        starting_indegree.append(out)
                length -= 1
        
        if len(res) < numCourses:
            return []

        return res
