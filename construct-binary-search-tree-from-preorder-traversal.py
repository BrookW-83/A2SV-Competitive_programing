# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder[0]

        left_val = []
        right_val = []

        for i in range(1, len(preorder)):
            if preorder[i] < root_val:
                left_val.append(preorder[i])
            
            else:
                right_val.append(preorder[i])
    

        root = TreeNode(root_val)
        root.left = self.bstFromPreorder(left_val)
        root.right = self.bstFromPreorder(right_val)


        return root