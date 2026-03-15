# 783.Minimum distance between BST nodes
#
# Given the root of a Binary Search Tree (BST), return the
# minimum difference between the values of any two different nodes in the tree.
#
# Example 1:
#
# Input: root = [4,2,6,1,3]
# Output: 1
#
# Example 2:
#
# Input: root = [1, 0, 48, null, null, 12, 49]
# Output: 1
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 105

class Solution:
    p = float('-inf')
    r = float('inf')
    def minDiffInBST(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return

        self.minDiffInBST(node.left)
        self.r = min([self.r, abs(node.val - self.p)])
        self.p = node.val
        self.minDiffInBST(node.right)

        return self.r