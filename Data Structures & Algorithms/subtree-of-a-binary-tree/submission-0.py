# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isIdentical(root, subroot):
            if not root and not subroot: return True
            if not root or not subroot: return False
            if root.val != subroot.val: return False

            return isIdentical(root.left,subroot.left) and isIdentical(root.right, subroot.right)
        
        q = deque([[root, subRoot]])
        while q:
            nodes = q.pop()
            if nodes[0]: 
                q.append([nodes[0].left, nodes[1]])
                q.append([nodes[0].right, nodes[1]])
            if isIdentical(nodes[0],nodes[1]): return True
        
        return False
