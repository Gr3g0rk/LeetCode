# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''Koren levo desno'''
        if root is None:
            return []
        return [root.val] + Solution.inorderTraversal(root.left) + Solution.inorderTraversal(root.right)
        
        
