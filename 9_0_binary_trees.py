class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_traversal(root):
    # Notice how the three different traversal only differs in where they process the node.
    # Time complexity is O(num of nodes), space complexity is O(h), where h is the max depth of the tree. This is because of the call-stack.
    if root:
        print('Preorder: %c' % root.data)
        tree_traversal(root.left)
        #print('Inorder: %c' % root.data)
        tree_traversal(root.right)
        #print('Postorder: %c' % root.data)


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
    tree_traversal(A)
