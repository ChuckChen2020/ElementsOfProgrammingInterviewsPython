from collections import namedtuple


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def k_balanced(k, root):
    # The namedtuple defind below will be used as a return, if the node is k-balanced, return None, else return the node itself.
    LRNodeCounts = namedtuple("LRNodeCounts", ("none_or_node", "count"))

    def count(node):
        if node == None:
            return LRNodeCounts(None, 0)
        leftResult = count(node.left)
        if leftResult.none_or_node:
            return leftResult
        rightResult = count(node.right)
        if rightResult.none_or_node:
            return rightResult

        return LRNodeCounts(node if abs(leftResult.count - rightResult.count) > k else None, leftResult.count + rightResult.count + 1)

    return count(root).none_or_node.data


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
    print(k_balanced(3, A))
