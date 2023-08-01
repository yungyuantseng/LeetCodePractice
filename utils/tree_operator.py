def find_max_depth(root) -> int:
    if root is None:
        return 0
    else:
        depth_left_tree = find_max_depth(root.left)
        depth_right_tree = find_max_depth(root.right)

        return max(depth_left_tree, depth_right_tree) + 1


def inorder_traversal(root) -> list:
    trace_result = []

    def trace(root):
        if root is None:
            return
        else:
            trace(root.left)
            trace_result.append(root.val)
            trace(root.right)
    trace(root)
    return trace_result

# TODO: finished preorder, postorder, levelorder
