# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        level = []
        def pre(root):
            if not root: return
            nonlocal level
            pre(root.left)
            level.append(root.val)
            pre(root.right)

        
        pre(root)
        for i in range(len(level)-1):
            if level[i]>=level[i+1]: return False

        return True