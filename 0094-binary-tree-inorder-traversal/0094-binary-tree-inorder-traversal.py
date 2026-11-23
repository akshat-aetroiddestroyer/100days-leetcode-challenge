# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # inorder traversal = left, node, right

        # RECURSIVE SOLUTION:
        # output = []
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     output.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # return output

        # ITERATIVE SOLUTION
        stack = []
        if root:
            stack.append((root, False))
        output = []
        while stack:
            node, visited = stack.pop()
            if not visited:
                # if node is unexplored
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))  # mark as explored
                if node.left:
                    stack.append((node.left, False))
            else:
                # print val once node has been explored
                output.append(node.val)
        return output