class DSU:
    def __init__(self, n):
        self.comps = n
        self.parent = [i for i in range(n)]
        self.size = [1]*(n) 
    def find(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        A = self.find(x)
        B = self.find(y)

        if A == B: return False
        self.comps -= 1
        
        if self.size[A] < self.size[B]:
            A,B = B, A
        self.size[A] += self.size[B]
        self.parent[B] = A
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1): return False
        dsu = DSU(n)
        for s,e in edges:
            if not dsu.union(s,e): return False
        p = dsu.find(0)
        for i in range(1,n):
            if dsu.find(i)!=p: return False
        return True