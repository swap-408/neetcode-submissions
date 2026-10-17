class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        
        visited = set()
        comp = 0

        for i in range(n):
            if i in visited: continue
            comp += 1
            q = deque([i])
            while q:
                cur = q.popleft()
                if cur in visited: continue
                visited.add(cur)

                for n in adj[cur]:
                    if n not in visited: q.append(n)
        
        return comp