class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        for p in prerequisites:
            indegree[p[0]] += 1
            adj[p[1]].append(p[0])
        q = deque()
        for i,d in enumerate(indegree):
            if d==0: q.append(i)

        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for node in adj[c]:
                indegree[node] -= 1
                if indegree[node]==0: q.append(node)
        
        if len(res) < numCourses:
            return False
        return True
        


