# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0

        # Get the height of left and right sub-trees
        leftDepth = self.diameterHelper(root.left)
        rightDepth = self.diameterHelper(root.right)

        # Get the diameter of left and irgh sub-trees
        lDiameter = self.diameterOfBinaryTree(root.left)
        rDiameter = self.diameterOfBinaryTree(root.right)

        # Return max of the following tree:
        # 1) Diameter of left subtree
        # 2) Diameter of right subtree
        # 3) Height of left subtree + height of right subtree +1
        return max(leftDepth + rightDepth, max(lDiameter, rDiameter))


    def diameterHelper(self, Node):
        if Node is None:
            return 0

        return 1 + max(self.diameterHelper(Node.left), self.diameterHelper(Node.right))
