"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        mp = {}
        q = deque([node])
        cnode = Node(node.val)
        mp[node] = cnode
        seen = set()
        while q:
            cur = q.popleft()
            if cur in seen: continue
            else: seen.add(cur)
            if cur not in mp:
                mp[cur] = Node(cur.val)
            for nei in cur.neighbors:
                if nei not in mp:
                    mp[nei] = Node(nei.val)
                mp[cur].neighbors.append(mp[nei])
                q.append(nei)
        return cnode