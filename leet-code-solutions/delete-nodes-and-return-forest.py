# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []

        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete:
                if node.left is None and node.right is None:
                    return None
                else:
                    if node.left:
                        res.append(node.left)
                    if node.right:
                        res.append(node.right)

                    return None

            return node

        val = dfs(root)
        if val:
            res.append(val)

        return res



