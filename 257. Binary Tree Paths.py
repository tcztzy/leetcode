class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

test_case1 = TreeNode(1)
test_case1.left = TreeNode(2)
test_case1.left.right = TreeNode(5)
test_case1.right = TreeNode(3)

class Solution:
    def binaryTreePaths(self, root):
        def travel(node):
            def get_path(node):
                if node.up is not None:
                    return get_path(node.up)+'->'+str(node.val)
                else:
                    return str(node.val)
            if node is not None:
                if node.left is None and node.right is None:
                    paths.append(get_path(node))
                if node.left is not None:
                    node.left.up = node
                    travel(node.left)
                if node.right is not None:
                    node.right.up = node
                    travel(node.right)
        paths = []
        if root is not None:
            root.up = None
            travel(root)
        return paths

if __name__ == '__main__':
    s = Solution()
    print(s.binaryTreePaths(test_case1))
