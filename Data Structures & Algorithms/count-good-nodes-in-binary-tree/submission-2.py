# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(node, high):
            if not node:
                return 0
            if node.val >= high:
                res.append(node.val)
            h = max(high, node.val)
            dfs(node.left, h)
            dfs(node.right, h)
        dfs(root, float('-inf'))
        print(res)
        return len(res)