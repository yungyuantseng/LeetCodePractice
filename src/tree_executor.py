import sys

sys.path.append('.')
from utils.tree_node import Node  # noqa
from utils.tree_operator import find_max_depth, inorder_traversal  # noqa


def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


if __name__ == '__main__':
    tree = build_tree()
    depth = find_max_depth(tree)
    print(f'Max depth of the tree is: {depth}')

    inorder = inorder_traversal(tree)
    print(f'Inorder trace the tree: {inorder}')
