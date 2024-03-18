# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def result(root, tmp):
            if not root:
                return None
            
            result(root.left, tmp)
            tmp += [root.val]
            result(root.right, tmp)

        tmp = []
        result(root, tmp)
        return tmp
