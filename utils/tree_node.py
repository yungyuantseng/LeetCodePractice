class Node():
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None

# start to build the tree
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print(root)

    while(root):
        print(root.val)
        root=root.left
