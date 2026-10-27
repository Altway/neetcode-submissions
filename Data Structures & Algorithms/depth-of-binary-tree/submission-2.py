# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        response = 0
        def dfs(node, l):
            nonlocal response           
            if not node:
                response = max(response, l)
                return 
            dfs(node.left, l+1)
            dfs(node.right, l+1)

        dfs(root, response)
        return response
        