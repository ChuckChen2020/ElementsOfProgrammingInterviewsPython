from collections import namedtuple
from math import floor, log2


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def largest_complete_subtree_size(root):
    PerfectCompleteSizeHeight = namedtuple(
        "PerfectCompleteHeight", ('perfect', 'complete', 'height', 'complete_subtree_height'))

    def traverse(node):
        if node == None:
            return PerfectCompleteSizeHeight(True, True, -1, -1)
        leftResult = traverse(node.left)
        rightResult = traverse(node.right)
        # Scenario 1:
        # left sub perfect, right sub complete, height the same => Complete
        if leftResult.perfect and rightResult.complete and leftResult.height == rightResult.height:
            is_complete = True
            is_perfect = rightResult.perfect
            complete_subtree_height = height = leftResult.height + 1
            return PerfectCompleteSizeHeight(is_perfect, is_complete, height, complete_subtree_height)
        # Scenario 2:
        # left sub complete, right sub perfect, l_height == (r_height + 1) => Complete
        elif leftResult.complete and rightResult.perfect and leftResult.height - rightResult.height == 1:
            is_complete, is_perfect = True, False
            complete_subtree_height = height = leftResult.height + 1
            return PerfectCompleteSizeHeight(is_perfect, is_complete, height, complete_subtree_height)
        # Scenario 3:
        # Aside from the above 2 scenario, the tree cannot be complete.
        else:
            is_complete, is_perfect = False, False
            height = max(leftResult.height, rightResult.height) + 1
            complete_subtree_height = max(
                leftResult.complete_subtree_height, rightResult.complete_subtree_height)
            return PerfectCompleteSizeHeight(is_perfect, is_complete, height, complete_subtree_height)

    return traverse(root).complete_subtree_height


if __name__ == '__main__':
    A = BinaryTreeNode('A')
    A.left = B = BinaryTreeNode('B')
    A.right = I = BinaryTreeNode('I')
    B.left = C = BinaryTreeNode('C')
    B.right = F = BinaryTreeNode('F')
    C.left = D = BinaryTreeNode('D')
    C.right = E = BinaryTreeNode('E')
    F.right = G = BinaryTreeNode('G')
    G.left = H = BinaryTreeNode('H')
    I.left = J = BinaryTreeNode('J')
    I.right = O = BinaryTreeNode('O')
    J.right = K = BinaryTreeNode('K')
    O.right = P = BinaryTreeNode('P')
    K.left = L = BinaryTreeNode('L')
    K.right = N = BinaryTreeNode('N')
    L.right = M = BinaryTreeNode('M')
    print(largest_complete_subtree_size(A))
