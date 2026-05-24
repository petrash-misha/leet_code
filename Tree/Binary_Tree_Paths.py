# 257.Binary Tree Paths
#
# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
#
# Example 1:
#
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#
# Example 2:
#
# Input: root = [1]
# Output: ["1"]
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def DFS(node, path, result):
    if node == None:
        return result

    local_path = path + [str(node.val)]
    if node.left == None and node.right == None:
        result.append("->".join(local_path))

    DFS(node.left, local_path, result)
    DFS(node.right, local_path, result)

    return result


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return DFS(root, [], [])