class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
    def find(self,x):
        if self.parent[x]==x: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)

        if px==py: return False
        self.parent[py] = px
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for e in edges:
            if not dsu.union(e[0],e[1]): return e
        return edges[-1]

