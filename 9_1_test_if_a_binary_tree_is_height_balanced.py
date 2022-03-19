import collections


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTreeHeightBalanced:
    def __init__(self):
        self.ans = True

    def height(self, node):
        if node.left == None and node.right == None:
            return 0
        h_left = 0 if node.left == None else self.height(node.left) + 1
        h_right = 0 if node.right == None else self.height(node.right) + 1
        if h_left - h_right not in (-1, 0, 1):
            self.ans = False
        return max(h_left, h_right)


def is_balanced_binary_tree(node):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(node):
        if node == None:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balanced(node.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(node.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(node).balanced


if __name__ == '__main__':
    root = A = BinaryTreeNode('A')
    A.left = B = BinaryTreeNode('B')
    A.right = K = BinaryTreeNode('K')
    B.left = C = BinaryTreeNode('C')
    B.right = H = BinaryTreeNode('H')
    C.left = D = BinaryTreeNode('D')
    C.right = G = BinaryTreeNode('G')
    H.left = I = BinaryTreeNode('I')
    H.right = J = BinaryTreeNode('J')
    D.left = E = BinaryTreeNode('E')
    D.right = F = BinaryTreeNode('F')
    K.left = L = BinaryTreeNode('L')
    K.right = O = BinaryTreeNode('O')
    L.left = M = BinaryTreeNode('M')
    L.right = N = BinaryTreeNode('N')
    is_height_balanced = BinaryTreeHeightBalanced()
    is_height_balanced.height(root)
    print(is_height_balanced.ans)
    print(is_balanced_binary_tree(root))
